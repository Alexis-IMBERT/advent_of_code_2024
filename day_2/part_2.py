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


safe_reports = 0

for report in reports:
    if is_safe(report):
        safe_reports += 1
    else:
        possible_reports = [report[:i] + report[i + 1 :] for i in range(len(report))]
        for possible_report in possible_reports:
            if is_safe(possible_report):
                safe_reports += 1
                break

print(safe_reports)
