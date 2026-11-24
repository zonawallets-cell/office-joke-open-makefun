"""Make the AI Judge Laugh: the Office Joke Open — make.fun entry.

Writes one line of office comedy to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Pure standard library only (os). The line is a fixed string: a calendar
that declines meetings on its owner's behalf, 79 characters, well inside
the gate's 1-200 character limit.

Why this line wins, against the judge's brief, most important first:
1. It is a joke about office life, not a complaint: the calendar acts,
   the owner benefits, nobody grumbles.
2. The laugh is earned in the last few words: "better boundaries than
   I do" turns a mundane calendar action into a confession.
3. The office detail is specific: a calendar declining a meeting, a
   thing every office worker has watched happen to them.
4. It is fresh: the calendar is given agency and a spine, a setup the
   crowded reply-all / printer / could-have-been-an-email tropes never
   use.
5. It reads cleanly in one pass, 79 characters, no word to cut.
"""

import os

LINE = "My calendar just declined a meeting for me. It has better boundaries than I do."

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: 1-200 UTF-8 chars, single line,
    not only whitespace. Raises ValueError on any violation.

    The gate is the only thing between the line and the judge: a file
    that fails it is listed with 0 and never judged, so every condition
    here mirrors the gate exactly, including the single-line rule the
    gate implies for a one-line joke.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d characters, got %d"
                         % (MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    # Validate first: a line that fails the gate must never reach disk.
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify the file holds exactly the validated line:
    # the judge reads the file, not the string in memory.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the validated line")
    print("wrote %d chars to %s (verified)" % (len(LINE), path))


if __name__ == "__main__":
    main()
