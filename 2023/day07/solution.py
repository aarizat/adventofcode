from collections import Counter

map_letters = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}
map_letters_2 = {'T': 'A', 'J': '0', 'Q': 'C', 'K': 'D', 'A': 'E'}

hand_kind = {
    '5': 7,
    '41': 6,
    '32': 5,
    '311': 4,
    '221': 3,
    '2111': 2,
    '11111': 1,
}

def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

def by_strong_kind(hand):
    counter = Counter(hand)
    key = ''.join((str(v) for _, v in counter.most_common()))
    return (hand_kind[key], [map_letters.get(ch, ch) for ch in hand])


def part_1():
    hands = [line.split(' ') for line in read_input('input.txt')]
    hands.sort(key=lambda pair: by_strong_kind(pair[0]))
    total = 0
    for pos, (_, bid) in enumerate(hands, start=1):
        total += pos * int(bid)
    print(total)


def by_strong_kind_2(hand):
    map_hand = ''.join((map_letters_2.get(ch, ch) for ch in hand))

    best_kind = 0
    for c in "98765432EDCA":
        new_hand = map_hand.replace('0', c)
        counter = Counter(new_hand)
        new_key = ''.join((f'{v}' for _, v in counter.most_common()))
        best_kind = max(best_kind, hand_kind[new_key])

    return (best_kind, list(map_hand))


def part_2():
    hands = [line.split(' ') for line in read_input('input.txt')]
    hands.sort(key=lambda pair: by_strong_kind_2(pair[0]))
    total = 0
    for pos, (_, bid) in enumerate(hands, start=1):
        total += pos * int(bid)
    print(total)


part_1()
part_2()
