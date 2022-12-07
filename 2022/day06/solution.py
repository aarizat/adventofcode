def part_1(file) -> int:
    text = file.readline()
    if any(len(set(text[i:(r := i+4)])) == 4 for i in range(len(text))):
        return r


def part_2(file) -> int:
    text = file.readline()
    if any(len(set(text[i:(r := i+14)])) == 14 for i in range(len(text))):
        return r

f = open('input.txt')
print(part_1(f)) # 1598
f = open('input.txt')
print(part_2(f)) # 2414