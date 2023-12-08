from itertools import cycle


def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.strip()


instructions, _, *raw_map = [line for line in read_input('input.txt')]
map_insts = {'L': 0, 'R': 1}
node_path = {item[0:3]: item[7:-1].split(', ') for item in raw_map}


def part_1():
    start = 'AAA'
    count = 0
    for inst in cycle(instructions):
        start = node_path[start][map_insts[inst]]
        count += 1
        if start == 'ZZZ':
            break
    print(count)


def part_2():
    start_points = [key for key in node_path if key.endswith('A')]
    count = 0
    for inst in cycle(instructions):
        for i in range(len(start_points)):
            start_points[i] = node_path[start_points[i]][map_insts[inst]]
        count += 1
        if all((point.endswith('Z') for point in start_points)):
            break
    print(count)


part_1()
part_2()