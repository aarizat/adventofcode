import re


PATTERN = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)')

def read_input(file):
    with open(file, mode='r') as fd:
        return fd.read()

def mul(a, b):
    return a * b


def solution1(text):
    return sum([eval(m) for m in re.findall(PATTERN, text)])


print(solution1(read_input('input.txt')))