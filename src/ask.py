"""Ask Mitra a question from the terminal.

Usage:
    python -m src.ask "When should fenoxaprop-p-ethyl be sprayed in dry direct-sown rice?"
    python -m src.ask              # interactive; empty line or Ctrl+C to quit
    python -m src.ask --crop potato "..."
"""
import argparse

import httpx

from src.answer import answer_question


def show(question, crop=None):
    res = answer_question(question, crop=crop)
    print(f"\n{res['answer']}\n")
    for note in (res["crop_note"], res["gate_detail"]):
        if note:
            print(note)
    print(res["sources_block"])
    t = res["timings"]
    gate = f"refused ({res['gate_reason']})" if res["gated"] else res["generator"]
    print(f"[{gate} | top_sim={res['top_similarity']:.4f} | retrieve {t['retrieve_s']}s | generate {t['generate_s']}s]\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("question", nargs="*")
    ap.add_argument("--crop", help="restrict retrieval to one crop, e.g. potato")
    args = ap.parse_args()

    try:
        run(args)
    except (httpx.ConnectError, ConnectionError) as e:  # ollama client raises either, depending on the call
        raise SystemExit(f"Cannot reach Ollama ({e}). Start it with `ollama serve` or the Ollama app.")


def run(args):
    if args.question:
        show(" ".join(args.question), args.crop)
        return
    try:
        while q := input("Question> ").strip():
            show(q, args.crop)
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == "__main__":
    main()
