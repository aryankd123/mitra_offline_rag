"""Block and record any non-loopback network access from this Python process (design R13).

Uses a CPython audit hook (sys.addaudithook), which sees every DNS lookup and socket connect.
This covers *our* process only (Chroma, LangChain, httpx). Ollama is a separate program, so the
Wi-Fi-off / no-egress test is still the real proof; this guard is evidence we can check on every run.
"""
import ipaddress
import sys

LOCAL_NAMES = {None, "", "localhost", "localhost.localdomain"}
_attempts = []
_installed = False


class OfflineViolation(OSError):
    """Raised instead of opening a non-loopback connection; OSError so libraries treat it as a network failure."""


def _is_loopback(host):
    if isinstance(host, bytes):
        host = host.decode(errors="replace")
    if host in LOCAL_NAMES:
        return True
    try:
        return ipaddress.ip_address(str(host).split("%")[0]).is_loopback
    except ValueError:
        return False


def _hook(event, args):
    if event == "socket.getaddrinfo":
        host = args[0]
    elif event == "socket.connect":
        address = args[1]
        if not isinstance(address, tuple):  # AF_UNIX path, not a network address
            return
        host = address[0]
    else:
        return
    if not _is_loopback(host):
        _attempts.append((event, str(host)))
        raise OfflineViolation(f"offline guard blocked {event} to {host!r}")


def install():
    """Idempotent; audit hooks cannot be removed once added."""
    global _installed
    if not _installed:
        sys.addaudithook(_hook)
        _installed = True


def installed():
    return _installed


def attempts():
    """Blocked (event, host) pairs since install()."""
    return list(_attempts)
