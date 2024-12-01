from collections import Counter


def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip('\n')

def input_to_array(path):
    left = []
    right = []
    for line in read_input(path):
        n1, n2 = line.split('   ')
        left.append(int(n1))
        right.append(int(n2))
    return left, right


def part_1():
    arr1, arr2 = input_to_array('input1.txt')
    total = 0
    arr2.sort()
    arr1.sort()
    for n1, n2 in zip(arr1, arr2):
        total += abs(n2 - n1)
    return total


def part_2():
    left_arr, right_arr = input_to_array('input1.txt')
    total = 0
    counter = Counter(right_arr)
    for num in left_arr:
        total += num * counter.get(num, 0)
    return total


print(part_1())
print(part_2())