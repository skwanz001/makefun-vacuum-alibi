"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "Lidar mapped the crumb as load-bearing. "
    "Removing it would collapse the kitchen. "
    "I am not insured for that."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify exactly what the gate will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "output mismatch"
    print(f"wrote {len(written)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
