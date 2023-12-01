map_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip('\n')


def solution1():
    total = 0
    for line in read_input('input.txt'):
        l_ptr, r_ptr = 0, len(line) - 1
        while not line[l_ptr].isdigit(): l_ptr += 1
        while not line[r_ptr].isdigit(): r_ptr -= 1
        total += int(line[l_ptr] + line[r_ptr])
    print(total)


def solution2():
    # TODO: complete task
    total = 0
    for line in read_input('input.txt'):
        ...


solution1()
solution2()