from pathlib import Path
import re

data_string = Path("day_3/data.txt").read_text("utf-8")

regex = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

matches = re.findall(regex, data_string)

count = 0
is_enabled = True
for match in matches:
    if match == "don't()":
        is_enabled = False
    elif match == "do()":
        is_enabled = True
    elif is_enabled:
        numbers = re.findall(r"\d+", match)
        a, b = map(int, numbers)
        count += a * b

print(count)
