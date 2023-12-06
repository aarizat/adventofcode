import re


def read_input(path):
    with open(path) as f:
        return f.read()


def part_1():
    content = read_input('input.txt')
    all_data = re.findall(r'\d+', content)
    lenght = len(all_data)//2
    time_distance = zip(all_data[:lenght], all_data[lenght:])

    total = 1
    for time, distance in time_distance:
        vel_holds = zip(range(int(time), -1, -1), range(0, int(time)+1))
        total *= sum([h * v  > int(distance) for h, v in vel_holds])
    print(total)


def part_2():
    content = read_input('input.txt')
    all_data = re.findall(r'\d+', content)
    lenght = len(all_data)//2
    time, distance = ''.join(all_data[:lenght]), ''.join(all_data[lenght:])

    vel_holds = zip(range(int(time), -1, -1), range(0, int(time)+1))
    total = sum([h * v  > int(distance) for h, v in vel_holds])
    print(total)


part_1()
part_2()
