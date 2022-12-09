import numpy as np
from itertools import product


def part_1(file) -> int:
    matrix = np.array([list(map(int, line)) for line in file.read().splitlines()])
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    for row, col in product(range(rows), range(cols)):
        tree = matrix[row, col]
        count +=  any([
            all(tree > matrix[row, :col]),  # left
            all(tree > matrix[:row, col]),  # top
            all(tree > matrix[row, col+1:]),  # right
            all(tree > matrix[row+1:, col])  # down
        ])
    return count


def part_2(file) -> int:
    matrix = np.array([list(map(int, line)) for line in file.read().splitlines()])
    rows, cols = len(matrix), len(matrix[0])
    distances = []
    for row, col in product(range(rows), range(cols)):
        tree = matrix[row, col]
        dist = 1
        for path in (matrix[row, col-1::-1], matrix[row-1::-1, col], matrix[row, col+1:], matrix[row+1:, col]):
            count = 0
            for t in path:
                count += 1
                if t >= tree:
                    break
            dist *= count
        distances.append(dist)
    return max(distances)


f = open('input.txt')
print(part_1(f)) # 1823
f = open('input.txt')
print(part_2(f)) # 211680