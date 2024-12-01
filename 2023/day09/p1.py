def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.strip()


def part_1():
    matrix = [list(map(int, line.split())) for line in read_input('input.txt')]

    total = 0
    for row in matrix:
        last_elms = [row[-1]]
        lenght = len(row)
        arr = [row]
        for i in range(lenght, -1, -1):
            new_row = [arr[-1][j+1]-arr[-1][j] for j in range(i-1)]
            arr.append(new_row)
            last_elms.append(new_row[-1])
            if all([elm == 0 for elm in new_row]):
                break
        total += sum(last_elms)
    print(total)

part_1()