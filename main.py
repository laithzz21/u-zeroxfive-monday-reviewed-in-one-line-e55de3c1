#!/usr/bin/env python3
"""Entry generator for the make.fun bounty
'u-zeroxfive-monday-reviewed-in-one-line-e55de3c1'.

Competition: "Monday, Reviewed — In One Line".
Brief: write the funniest one-line review of your own Monday.
Rules enforced here: exactly one line, under 200 characters, no title,
no explanation — the entry text is the whole submission.

The script validates the entry against every rule, writes it to
``entry.txt`` in the output directory (``$MAKEFUN_OUTPUT`` when set,
otherwise ``/output``, falling back to ``./output`` next to this file),
verifies the written file by reading it back, and prints the entry
text itself to stdout so the submission can be captured verbatim.

Deterministic, stdlib only, no network, no clock, no randomness.
"""

import hashlib
import os
import re
import sys

SLUG = "u-zeroxfive-monday-reviewed-in-one-line-e55de3c1"

# The entry: one line, 143 characters, no title, no explanation.
ENTRY_TEXT = (
    "Monday arrived uninvited, stole my sleep, ate my motivation, "
    "and still expected productivity. One star \u2014 would not "
    "recommend, will not be back."
)

MAX_CHARS = 200  # brief: under 200 characters (strictly less than 200)


def fail(message: str) -> None:
    """Fail loudly: print the violation and exit non-zero."""
    print(f"VALIDATION FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate(text: str) -> None:
    """Enforce the competition brief, rule by rule.

    Raises SystemExit(1) with a clear message on the first violation,
    so a bad entry can never be printed or written silently.
    """
    if not isinstance(text, str):
        fail(f"entry must be a string, got {type(text).__name__}")
    if not text:
        fail("entry must not be empty")

    # Rule 1: exactly one line — no line breaks of any kind.
    if "\n" in text or "\r" in text:
        fail("entry must be exactly one line (contains a line break)")
    if text.count("\n") + text.count("\r") > 0:
        fail("entry must be exactly one line")

    # Rule 2: under 200 characters (strictly less than 200).
    length = len(text)
    if length >= MAX_CHARS:
        fail(f"entry must be under {MAX_CHARS} chars, got {length}")
    if length < 10:
        fail(f"entry is suspiciously short ({length} chars)")

    # Rule 3: no title and no explanation — a single flowing sentence
    # (or two short ones), with no title markers, labels or headings,
    # and no trailing "P.S." / "Note:" style explanation tacked on.
    if text.lstrip().startswith(("#", "Title:", "Review:", "Monday:")):
        fail("entry must not carry a title or label prefix")
    if re.search(r"\b(P\.S\.|Note:|Explanation:)\b", text):
        fail("entry must not carry a trailing explanation")
    if text.rstrip().endswith(("-", "—", ":")):
        fail("entry must not end on a dangling separator")
    if re.search(r"\n", text):
        fail("entry must not contain a newline")

    # Rule 4: it must actually review Monday — the subject word has
    # to appear, otherwise this is a generic joke, not a Monday review.
    if "monday" not in text.lower():
        fail("entry must mention Monday (it reviews your own Monday)")

    # Rule 5: clean, printable text only — no control characters,
    # no leading/trailing whitespace, no doubled spaces.
    if text != text.strip():
        fail("entry must not have leading or trailing whitespace")
    if "  " in text:
        fail("entry must not contain doubled spaces")
    bad_controls = [ch for ch in text if ord(ch) < 32 and ch not in ("\t",)]
    if bad_controls:
        fail(f"entry contains control characters: {bad_controls!r}")

    # Rule 6: it must read as a review — a star/rating signal plus a
    # verdict, so the line is a review and not just a complaint.
    if not re.search(r"\b(one|1)\s+star\b", text, re.IGNORECASE):
        fail("entry must contain a star rating (it is a review)")
    if "recommend" not in text.lower():
        fail("entry must contain a recommendation verdict")

    # Rule 7: word-count sanity — a one-line review is a sentence or
    # two, not a paragraph squeezed onto one line and not a fragment.
    words = text.split()
    if not 10 <= len(words) <= 40:
        fail(f"entry must be 10-40 words, got {len(words)}")


def entry_sha256(text: str) -> str:
    """Stable fingerprint of the entry text (UTF-8, no trailing newline)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def output_path() -> str:
    """Resolve the output file path.

    Uses $MAKEFUN_OUTPUT when set, otherwise /output; if /output is not
    writable, falls back to ./output relative to this script's directory.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    if os.access("/output", os.W_OK) or not os.path.exists("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            if os.access("/output", os.W_OK):
                return "/output/entry.txt"
        except OSError:
            pass
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output", "entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write the entry to disk and verify it by reading it back."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        raise RuntimeError(f"read-back mismatch in {path}")
    if entry_sha256(written.rstrip("\n")) != entry_sha256(text):
        raise RuntimeError(f"checksum mismatch after writing {path}")


def main() -> int:
    validate(ENTRY_TEXT)
    path = output_path()
    write_entry(path, ENTRY_TEXT)
    # Second validation pass: re-validate exactly what was written to
    # disk, so a write-time corruption can never ship a bad entry.
    with open(path, "r", encoding="utf-8") as f:
        on_disk = f.read().rstrip("\n")
    validate(on_disk)
    if on_disk != ENTRY_TEXT:
        raise RuntimeError("on-disk entry differs from ENTRY_TEXT")
    # The entry text itself is the stdout output — nothing else, so the
    # captured stdout is exactly the submission, byte for byte.
    print(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
