# AWS offline test (Stage 8 stand-in, D-46)

Goal: prove two claims on a machine that isn't the dev laptop.
1. **Clean install** — the README steps work from scratch.
2. **No internet at question time** — with all outbound traffic removed, the eval and the web page still work.

It also gives a second set of latency numbers (CPU only — the AWS free plan has no GPU instances).

Expected cost: covered by the free-plan credits if you **terminate the instance the same day**. Check Billing → Free Tier / Credits before and after.

---

## 1. Launch the instance (EC2 console)

| Setting | Value |
|---|---|
| AMI | Ubuntu Server 24.04 LTS (ships Python 3.12) |
| Instance type | `m7i-flex.large` (2 vCPU, 8 GiB; free-plan eligible for accounts created after 15 Jul 2025) |
| Key pair | create one, download the `.pem` |
| Storage | 20 GiB gp3 (models ≈ 1.1 GB, +3.3 GB with gemma3:4b; Python packages ≈ 1 GB) |
| Security group | inbound: SSH (22) from **My IP** only. Outbound: leave the default for now |

Do **not** open port 8000 to the internet; the web page is reached through an SSH tunnel (step 5).

From Windows PowerShell (OpenSSH is built into Windows 10):

```powershell
ssh -i C:\path\to\key.pem ubuntu@<public-ip>
```

If ssh complains the key permissions are too open: `icacls C:\path\to\key.pem /inheritance:r /grant:r "$($env:USERNAME):(R)"`.

## 2. Install (internet still on)

Before this, commit and push your latest code from the laptop — the instance gets only what is on GitHub. If the repo is private, `git clone` asks for a GitHub username and a personal access token (not your password).

```bash
sudo apt update && sudo apt install -y python3.12-venv git
curl -fsSL https://ollama.com/install.sh | sh        # installs and starts the ollama service
ollama pull nomic-embed-text && ollama pull gemma3:1b # optionally gemma3:4b (fits in 8 GiB RAM, slow)

git clone https://github.com/aryankd123/mitra_offline_rag.git
cd mitra_offline_rag
python3.12 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 3. Copy the documents (from your laptop, in a second PowerShell window)

PDFs are not in git. They stay on this private instance and are deleted with it.

```powershell
scp -i C:\path\to\key.pem -r data\raw ubuntu@<public-ip>:~/mitra_offline_rag/data/
```

Then on the instance build the index from scratch (this also tests ingest on a clean machine; embedding 595 chunks on CPU takes several minutes):

```bash
python -m src.ingest           # expect: 164 pages -> 595 chunks
```

## 4. Cut the internet

EC2 console → Security Groups → your group → **Outbound rules** → delete the "All traffic 0.0.0.0/0" rule (and the `::/0` one if present) → save.
Security groups are stateful, so your SSH session keeps working.

Check that it really is cut (both must fail):

```bash
curl -m 5 https://ollama.com ; echo "exit=$?"     # expect a timeout / non-zero exit
ollama pull nomic-embed-text ; echo "exit=$?"     # pull always contacts the registry -> expect a network error
```

Save the output — it's part of the evidence.

## 5. Run the tests offline

```bash
python -m eval.run_eval --split all --offline-guard --no-log          # retrieval + gate; must print "Offline guard: PASS"
python -m eval.run_eval --split dev --generate --offline-guard        # answers + latency -> eval/stage6_answers_dev.md
MITRA_GENERATOR_MODEL=gemma3:4b python -m eval.run_eval --split dev --generate --no-log   # optional, if 4b was pulled
python -m src.api &                                                     # web server on 127.0.0.1:8000
```

Retrieval metrics should equal the laptop's (dev R@5 0.75, test 0.80). If they differ slightly, Chroma's HNSW index can be the cause — note it, don't hide it.

Web page through an SSH tunnel (from your laptop):

```powershell
ssh -i C:\path\to\key.pem -L 8000:127.0.0.1:8000 ubuntu@<public-ip>
# then open http://127.0.0.1:8000 in your browser and ask a few questions
```

## 6. Record and clean up

- Copy results back: `scp -i key.pem ubuntu@<ip>:~/mitra_offline_rag/eval/stage6_answers_dev.md eval\stage8_aws_answers_dev.md`
- Note in `DECISIONS.md`: instance type, region, `lscpu` model name, the failed `curl`/`ollama pull` outputs, offline-guard PASS, retrieval metrics, latency p50/p95 for each model.
- **Terminate** the instance (EC2 → Instances → Instance state → Terminate). Stopping keeps the disk, which still uses credits and still holds the PDFs.

## Unverified details (check when you do it)

- Exact Ubuntu AMI name in your region's list and whether `python3.12-venv` is already installed.
- Whether 20 GiB of gp3 storage is fully covered by the free plan in your region (it is billed from credits either way).
