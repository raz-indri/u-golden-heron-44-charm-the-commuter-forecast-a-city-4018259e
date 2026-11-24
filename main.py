"""Charm the Commuter: Forecast a City That Isn't.

The joke: Wobblewick is a made-up city where the weather itself joins the
commute. The forecast keeps the familiar rhythm of a real broadcast
("sunny spells, light drizzle...") then bends it — the drizzle is confetti,
and the perpetually late 8:04 bus makes up for it with a driver handing out
umbrellas. A bored commuter at a rainy bus stop gets a small, warm surprise
instead of another grey morning.
"""

import os
from pathlib import Path

LINE = (
    "Wobblewick: sunny spells with a light drizzle of confetti — "
    "the 8:04 bus is late again, but the driver is handing out umbrellas."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
