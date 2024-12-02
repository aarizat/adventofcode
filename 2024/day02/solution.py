from itertools import pairwise


def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip('\n')


def part_1(data):
    total = 0
    for str_report in data:
        report = [int(num) for num in str_report.split(' ')]
        unsafe = False
        increase = decrease = False
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if abs(diff) > 3 or diff == 0:
                unsafe = True
                break
            elif diff < 0:
                decrease = True
            else:
                increase = True
        if unsafe  or (decrease and increase):
            continue
        total += 1
    return total


def is_report_valid(row):
    diffs = [b-a for a, b in pairwise(row)]
    for diff in diffs:
        if abs(diff) > 3 or diff == 0:
            return False
    increasing = all([diff > 0 for diff in diffs])
    decreasing = all([diff < 0 for diff in diffs])
    if not (increasing or decreasing):
        return False
    return True


def part_2(data):
    total = 0
    for str_report in data:
        report = [int(s) for s in str_report.split()]
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)
            if is_report_valid(report_copy):
                total += 1
                break
    return total


print(part_1(read_input('input.txt')))
print(part_2(read_input('input.txt')))