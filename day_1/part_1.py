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
list1 = sorted(list1)
list2 = sorted(list2)


somme = 0
while list1:
    list1_element = list1.pop(0)
    list2_element = list2.pop(0)
    distance = abs(list1_element - list2_element)
    somme += distance

print(somme)
