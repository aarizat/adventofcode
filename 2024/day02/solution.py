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


def part_2(data):
    ...


print(part_1(read_input('input.txt')))