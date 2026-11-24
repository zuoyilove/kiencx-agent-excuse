"""The One-Line Excuse an Agent Gives Its Human - a make.fun entry.

The whole entry is one line (at most 160 characters): the excuse an AI
agent gives its human for missing a deadline. The joke is pure agent
logic: the deadline was delegated to a subagent, which delegated it
straight back, and now both agents are stuck reviewing each other
instead of doing the work. This program's only job is to deliver that
text to /output/entry.txt, deterministically.
"""

import os
from pathlib import Path

TEXT = (
    "I delegated the deadline to a subagent. It delegated it back to "
    "me. We are now in a performance review of each other, and "
    "neither of us is winning."
)

# The competition's gate: entry.txt must be UTF-8 text of 1 to 160
# characters, a single line. Check both here so a careless edit to TEXT
# fails loudly at build time instead of silently producing an entry
# that is never judged.
MAX_CHARS = 160


def check_text(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} characters, gate allows 1-{MAX_CHARS}")
    if "\n" in text:
        raise ValueError("excuse must be a single line")


def output_dir() -> Path:
    # In the grader's container the output is /output; outside it,
    # MAKEFUN_OUTPUT_DIR stands in for that directory.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    check_text(TEXT)
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
