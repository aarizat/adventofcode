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

products_second = {
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
        accum = 0
        for line in f:
            elf_shot, my_shot = line.split()
            accum += scores.get(my_shot)
            accum += products.get((elf_shot, my_shot))
        return accum


def part_2(file: str) -> int:
    with open(file, mode='r') as f:
        accum = 0
        for line in f:
            elf_shot, my_shot = line.split()
            a, b = products_second.get((elf_shot, my_shot))
            accum += products.get((a, b))
            accum += scores.get(b)
        return accum

print(part_1("input.txt")) # 13924
print(part_2("input.txt")) # 13448
