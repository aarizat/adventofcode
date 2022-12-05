from operator import methodcaller as mc


def part_1(file: str) -> int:
    with open(file, mode="r") as f:
        count = 0
        for line in f.read().splitlines():
            l, r = map(mc('split', '-'), line.split(','))
            r1, r2 = list(map(int, l)), list(map(int, r))
            if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
                count += 1
        return count


def part_2(file: str) -> int:
    with open(file, mode="r") as f:
        count = 0
        for line in f.read().splitlines():
            l, r = map(mc('split', '-'), line.split(','))
            r1, r2 = list(map(int, l)), list(map(int, r))
            if max(r1[0], r2[0]) <= min(r1[1], r2[1]):
                count += 1
        return count

print(part_1("input.txt")) # 524
print(part_2("input.txt")) # 798
