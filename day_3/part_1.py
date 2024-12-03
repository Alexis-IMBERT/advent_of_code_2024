from pathlib import Path
import re

data_string = Path("day_3/data.txt").read_text("utf-8")


matches = re.findall(r"mul\(\d+,\d+\)", data_string)

count = 0
for match in matches:
    numbers = re.findall(r"\d+", match)
    a, b = map(int, numbers)
    count += a * b
print(count)
