import re


def part_1(file: str) -> int:
    with open(file, mode="r") as f:
        count = 0
        for line in f.read().splitlines():
            a, b, x, y = map(int, re.split(',|-', line))
            if (a >= x and b <= y) or (x >= a and y <= b):
                count += 1
        return count


def part_2(file: str) -> int:
    with open(file, mode="r") as f:
        count = 0
        for line in f.read().splitlines():
            a, b, x, y = map(int, re.split(',|-', line))
            if max(a, x) <= min(b, y):
                count += 1
        return count


print(part_1("input.txt")) # 524
print(part_2("input.txt")) # 798
