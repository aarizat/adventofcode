import re


bag_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

color_pattern = r'\d+ (?:blue|red|green)'

def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip('\n')


def part_1():
    total = 0
    for line in read_input('input.txt'):
        possible = True
        game, sets = line.split(':')
        list_of_sets = [pair.split(' ') for pair in re.findall(color_pattern, sets)]
        for amount, color in list_of_sets:
            if int(amount) > bag_cubes[color]:
                    possible = False
        if possible:
            total += int(game.split(' ')[-1])
    print(total)


def part_2():
    total = 0
    for line in read_input('input.txt'):
        _, sets = line.split(':')
        list_of_sets = [pair.split(' ') for pair in re.findall(color_pattern, sets)]
        maximums = 1
        for color in bag_cubes:
            max_amount = 0
            for count, clr in list_of_sets:
                if color == clr:
                    max_amount = max(max_amount, int(count))
            maximums *= max_amount
        total += maximums
    print(total)


part_1()
part_2()