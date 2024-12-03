from pathlib import Path

reports = Path("day_2/data.txt").read_text(encoding="utf-8").split("\n")
reports = [list(map(int, report.split(" "))) for report in reports]


def is_incrising(liste: list[int]) -> bool:
    for i in range(len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
    return True


def is_decreasing(liste: list[int]) -> bool:
    for i in range(len(liste) - 1):
        if liste[i] < liste[i + 1]:
            return False
    return True


def is_safe(report: list[list[int]]) -> bool:
    if not is_incrising(report) and not is_decreasing(report):
        return False
    for i in range(len(report) - 1):
        value_difference = abs(report[i] - report[i + 1])
        if value_difference < 1 or value_difference > 3:
            return False
    return True


print(sum([is_safe(report) for report in reports]))
