import re


PATTERN_1 = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
PATTERN_2 = re.compile(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))")

def read_input(file):
    with open(file, mode='r') as fd:
        return fd.read()


def mul(a, b):
    return a * b


def solution1(text):
    return sum([eval(m) for m in re.findall(PATTERN_1, text)])

def solution2(text):
    total = 0
    enabled = True
    for m, do, dont in re.findall(PATTERN_2, text):
        if do == "do()":
            enabled = True
        elif dont == "don't()":
            enabled = False

        if enabled and m:
            total += eval(m)
    return total


print(solution1(read_input('input.txt')))
print(solution2(read_input('input.txt')))
