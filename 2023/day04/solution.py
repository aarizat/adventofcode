import re


def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip('\n')


def part_1():
    total = 0
    for line in read_input('input.txt'):
        _, card_numbers = line.split(': ')
        winnings, have = card_numbers.split(' | ')
        winnings_set, have_set = set(re.findall(r'\d+', winnings)), set(re.findall(r'\d+', have))
        commons = winnings_set & have_set
        total += int(1 * 2 ** (len(commons) - 1))
    print(total)


def part_2():
    list_of_pairs = []
    for line in read_input('input.txt'):
        _, card_numbers = line.split(': ')
        winnings, have = card_numbers.split(' | ')
        winnings_set, have_set = set(re.findall(r'\d+', winnings)), set(re.findall(r'\d+', have))
        matches = winnings_set & have_set
        list_of_pairs.append([1, len(matches)])
    for i, pair in enumerate(list_of_pairs, start=1):
        for item in list_of_pairs[i:pair[1]+i]:
            item[0] += pair[0]
    print(sum(count for count, _ in list_of_pairs))


part_1()
part_2()

