from collections import deque


def part_1(file) -> str:
    arrang, movements = file.read().split('\n\n')
    matrix = [list(line[1:len(line):4]) for line in arrang.split('\n')][::-1]
    stacks = [[item for item in row if item.strip()] for row in zip(*matrix)]
    for mov in movements.split('\n'):
        m, f, t = map(int, mov.split()[1::2])
        for _ in range(m):
            stacks[t-1].append(stacks[f-1].pop())

    return "".join(stack.pop() for stack in stacks)


def part_2(file) -> str:
    arrang, movements = file.read().split('\n\n')
    matrix = [list(line[1:len(line):4]) for line in arrang.split('\n')][::-1]
    stacks = [[item for item in row if item.strip()] for row in zip(*matrix)]
    for mov in movements.split('\n'):
        m, f, t = map(int, mov.split()[1::2])
        tmp = deque()
        for _ in range(m):
            tmp.appendleft(stacks[f-1].pop())
        stacks[t-1].extend(tmp)
    return "".join(stack.pop() for stack in stacks)


file = open('input.txt')
print(part_1(file)) # TLFGBZHCN
file = open('input.txt')
print(part_2(file)) # QRQFHFWCL
