from collections import defaultdict
from math import prod


def parse_line(line):
    return {
        "items": [int(num) for num in line[1][18:].split(',')],
        "op": lambda old: eval(line[2][19:]),
        "test": lambda x: x % int(line[3][21:]) == 0,
        "testnum": int(line[3][21:]),
        "pass": {
            True: int(line[4][29:]),
            False: int(line[5][30:])
        }
    }


def part_1(file):
    monkeys = [
        parse_line(chunk.split('\n'))
        for chunk in file.read().split('\n\n')
    ]
    active = defaultdict(int)

    for _ in range(20):
        for ix, monkey in enumerate(monkeys):
            for item in monkey['items']:
                active[ix] += 1
                new = monkey['op'](item) // 3
                test = monkey['test'](new)
                to = monkey['pass'][test]
                monkeys[to]['items'].append(new)
            monkey['items'] = []
    r = sorted(active.values(), reverse=True)
    return r[0] * r[1]


def part_2(file):
    monkeys = [
        parse_line(chunk.split('\n'))
        for chunk in file.read().split('\n\n')
    ]
    active = defaultdict(int)
    mod = prod(monkey['testnum'] for monkey in monkeys)

    for _ in range(10_000):
        for ix, monkey in enumerate(monkeys):
            for item in monkey['items']:
                active[ix] += 1
                new = monkey['op'](item) % mod
                test = monkey['test'](new)
                to = monkey['pass'][test]
                monkeys[to]['items'].append(new)
            monkey['items'] = []
    r = sorted(active.values(), reverse=True)
    return r[0] * r[1]


f = open('input.txt')
print(part_1(f))
f = open('input.txt')
print(part_2(f))