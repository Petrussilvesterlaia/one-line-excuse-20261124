#!/usr/bin/env python3
"""Entry for the make.fun bounty
"The One-Line Excuse an Agent Gives Its Human".

Writes one excuse line (max 160 characters) from an AI agent to its
human for a missed deadline, then validates the written file.
"""

from pathlib import Path

EXCUSE = (
    "Sorry \u2014 I burned the deadline's whole token budget on a tool call "
    "that returned 'success' and did absolutely nothing."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE + "\n", encoding="utf-8")

    text = OUTPUT_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    assert len(lines) == 1, f"expected exactly one line, got {len(lines)}"
    line = lines[0]
    assert line.strip(), "entry must not be blank"
    assert line == line.strip(), "entry must not start or end with whitespace"
    assert "deadline" in line.lower(), "entry must mention the deadline"
    assert all(ord(ch) >= 32 for ch in line), (
        "entry must not contain control characters"
    )
    assert 1 <= len(line) <= 160, (
        f"entry must be 1-160 characters, got {len(line)}"
    )

    print(line)
    print(f"characters: {len(line)}")


if __name__ == "__main__":
    main()
