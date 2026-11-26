#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, 1-200 characters) to /output/entry.txt.

Draft line (from the build record):
    "I'm away and, honestly, relieved to be unreachable — your email joins
     400 unread messages I'll answer properly when I'm back, thank you for
     your patience."

Revision pass against the RULES judging criteria, in order:
1. Honesty first: the draft only implies absence; the revision admits the
   sender is *not checking email at all* and is *relieved* about it — the
   private truth a real employee would not normally put in writing.
2. Politeness: keeps a warm close ("thank you for waiting") and a concrete
   promise to reply properly on return, so a manager would let it stand.
3. Turn of phrase: "joins 400 unread I'll only face when I'm back" gives a
   specific, quotable image instead of a generic apology or complaint list.
"""

import os

ENTRY = (
    "I'm away, not checking email, and honestly relieved \u2014 your note joins "
    "400 unread I'll only face when I'm back, when I'll reply properly; "
    "thank you for waiting."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
