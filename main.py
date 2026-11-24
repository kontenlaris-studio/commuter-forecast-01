"""Charm the Commuter entry: Port Meridian — fog, umbrella showers, striking tide."""

import os

JOKE = (
    "Port Meridian forecast: canal escalators fogged until nine, umbrella "
    "showers at noon, and the Moon District ferry is delayed — the tide "
    "is unionizing again."
)

CHAR_COUNT = len(JOKE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
