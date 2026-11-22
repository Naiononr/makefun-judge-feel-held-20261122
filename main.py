#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to /output/entry.txt: a second-person scene of
being carried upstairs asleep, your head against a shoulder, the door
already open and the bed already turned down — written to leave its
reader held, quiet, with nothing to prove and nothing to carry. The
text is fixed and deterministic: the same words every run. Pure
standard library, no network.
"""

from pathlib import Path
import os
import tempfile

TEXT = (
    "You fell asleep in the back seat, and now someone is carrying you "
    "up the stairs, your head against their shoulder. The door is "
    "already open, the bed already turned down, and tonight nothing in "
    "the house is yours to carry."
)

# The scene is the entry: its exact wording and length are fixed.
EXPECTED_CHARS = 221


def main() -> None:
    assert len(TEXT) == EXPECTED_CHARS, f"scene changed: {len(TEXT)} chars"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Write atomically: a crash mid-write must never leave a partial file.
    fd, tmp = tempfile.mkstemp(dir=out.parent, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(TEXT)
        os.replace(tmp, out)
    except BaseException:
        os.unlink(tmp)
        raise


if __name__ == "__main__":
    main()
