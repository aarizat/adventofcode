
def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.strip()


def hash_string(string) -> int:
    current = 0
    for ch in string:
        current = ((current + ord(ch)) * 17) % 256
    return current


def part_1():
    total = 0
    arr_string = next(read_input("input.txt")).split(',')
    for string in arr_string:
        total += hash_string(string)
    print(total)


part_1()