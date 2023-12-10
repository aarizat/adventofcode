def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.strip()


def part_2():
    matrix = [list(map(int, line.split())) for line in read_input('input.txt')]

    total = 0
    for row in matrix:
        first_elms = [row[0]]
        arr = [row]
        for i in range(len(row), -1, -1):
            new_row = [arr[-1][j+1]-arr[-1][j] for j in range(i-1)]
            arr.append(new_row)
            first_elms.append(new_row[0])
            if all([elm == 0 for elm in new_row]):
                break
        for i in range(-1, -len(first_elms), -1):
            first_elms[i-1] -= first_elms[i]
        total += first_elms[0]
    print(total)


part_2()
