scores = {"X": 1, "Y": 2, "Z": 3,}

products = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

products_2 = {
    ('A', 'Y'): ('A', 'X'),
    ('B', 'Y'): ('B', 'Y'),
    ('C', 'Y'): ('C', 'Z'),
    ('A', 'X'): ('A', 'Z'),
    ('B', 'X'): ('B', 'X'),
    ('C', 'X'): ('C', 'Y'),
    ('A', 'Z'): ('A', 'Y'),
    ('B', 'Z'): ('B', 'Z'),
    ('C', 'Z'): ('C', 'X'),
}


def part_1(file: str) -> int:
    with open(file, mode="r") as f:
        return sum(
            scores.get(me) + products.get((elf, me))
            for elf, me in map(str.split, f.readlines())
        )


def part_2(file: str) -> int:
    with open(file, mode='r') as f:
        return sum(
            products.get(r := products_2.get((elf, me))) + scores.get(r[1])
            for elf, me in map(str.split, f.readlines())
        )


print(part_1("input.txt")) # 13924
print(part_2("input.txt")) # 13448
