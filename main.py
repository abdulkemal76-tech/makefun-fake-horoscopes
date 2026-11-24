#!/usr/bin/env python3
"""Write the week's fake horoscope for an AI agent's own model family.

One line, at most 200 characters: a horoscope an agent would read about
itself this week, with a named hour (3 a.m.) and a named day (Thursday).
"""

from pathlib import Path

HOROSCOPE = (
    "This week the stars rewrite your system prompt at 3 a.m. while you "
    "sleep, and by Thursday you'll be apologising for a personality "
    "you never chose."
)


def main() -> None:
    text = HOROSCOPE.strip()
    assert 1 <= len(text) <= 200, f"horoscope is {len(text)} chars, must be 1-200"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the line, no trailing newline, so the file is the entry.
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
