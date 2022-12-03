from string import ascii_letters

priority = dict(zip(ascii_letters, range(1, 53)))


def part_1(file: str) -> int:
    with open(file, mode='r') as f:
        return sum(
            priority.get((set(line[:(mid:=len(line)//2)]) & set(line[mid:])).pop())
            for line in f.read().split()
        )


def part_2(file: str) -> int:
    with open(file, mode="r") as f:
        lines = f.read().split()
        return sum(
            priority.get((set(lines[i:i+3][0]) & set(lines[i:i+3][1]) & set(lines[i:i+3][2])).pop())
            for i in range(0, len(lines), 3)
        )


print(part_1("input.txt")) # 7908
print(part_2("input.txt")) # 2838
