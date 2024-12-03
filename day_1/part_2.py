from pathlib import Path

list1, list2 = zip(
    *[
        (item[0], item[1])
        for item in [
            list(map(int, line.split("   ")))
            for line in Path("day_1/data.txt").read_text(encoding="utf-8").split("\n")
        ]
    ]
)


print(sum([element * list2.count(element) for element in list1]))
