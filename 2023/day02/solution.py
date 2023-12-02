bag_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip('\n')


def part_1():
    total = 0
    for line in read_input('input.txt'):
        possible = True
        game, subsets = line.split(':')
        for subset in subsets.split(';'):
            for pair in subset.strip().split(','):
                count, color = pair.strip().split(' ')
                if int(count) > bag_cubes[color]:
                    possible = False
        if possible:
            total += int(game.split(' ')[-1])
    print(total)


def part_2():
    total = 0
    for line in read_input('input.txt'):
        _, subsets = line.split(':')
        list_of_sets = []
        for subset in subsets.split(';'):
            for pair in subset.strip().split(','):
                list_of_sets.append(pair.strip().split(' '))
        maximums = 1
        for color in bag_cubes:
            max_amount = 0
            for pair in list_of_sets:
                if color == pair[1]:
                    max_amount = max(max_amount, int(pair[0]))
            maximums *= max_amount
        total += maximums
    print(total)


# part_1()
part_2()