"""Write the chosen one-line entry for make.fun bounty
u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

Deterministic: writes exactly one line (no trailing newline) to
/output/entry.txt on every run.
"""

from pathlib import Path

ENTRY = (
    "Today my agent checked a repo was safe by reading its own files, "
    "got flagged as a security risk for reading them, "
    "and now waits for my permission to exist."
)

# Gate: /output/entry.txt must be UTF-8 text of 1-200 characters.
# This line is 155 characters (verified locally), one line, no newline.


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
