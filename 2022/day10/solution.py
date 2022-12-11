from itertools import product


def part_1(file) -> int:
    ops = []
    X = 1

    for line in file.read().splitlines():
        o = line.split()[0]

        if o == 'noop':
            ops.append(X)
        else:
            ops.extend([X, X])
            X += int(line.split()[1])
    ops.append(X)
    return sum(ix*x for ix, x in list(enumerate(ops, start=1))[19::40])


def part_2(file) -> int:
    ops = []
    X = 1

    for line in file.read().splitlines():
        o = line.split()[0]

        if o == 'noop':
            ops.append(X)
        else:
            ops.extend([X, X])
            X += int(line.split()[1])
    ops.append(X)

    for i, j in product(range(0, len(ops), 40), range(40)):
        print(end = "##" if abs(ops[i + j] - j) <= 1 else "  ")


file = open('input.txt')
print(part_1(file)) # 13140
file = open('input.txt')
print(part_2(file))  # EKRHEPUZ