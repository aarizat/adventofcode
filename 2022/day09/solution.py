def part_1(file) -> int:
    VISITEDS = set([(0, 0)])
    H, T = [0, 0], [0, 0]

    for line in file.read().splitlines():
        mov, steps = line.split()
        for _ in range(int(steps)):
            x = 1 if mov == "R" else -1 if mov == "L" else 0
            y = 1 if mov == "U" else -1 if mov == "D" else 0

            H[0] += x
            H[1] += y

            dx = H[0] - T[0]
            dy = H[1] - T[1]

            if abs(dx) > 1 or abs(dy) > 1:
                if dx == 0:
                    T[1] += 1 if dy > 0 else -1
                elif dy == 0:
                    T[0] += 1 if dx > 0 else -1
                else:
                    T[0] += 1 if dx > 0 else -1
                    T[1] += 1 if dy > 0 else -1

            VISITEDS.add(tuple(T))
    return len(VISITEDS)


def part_2(file) -> int:
    VISITEDS = set([(0, 0)])
    P = [[0, 0] for _ in range(10)]

    for line in file.read().splitlines():
        mov, steps = line.split()
        for _ in range(int(steps)):
            x = 1 if mov == "R" else -1 if mov == "L" else 0
            y = 1 if mov == "U" else -1 if mov == "D" else 0

            P[-1][0] += x
            P[-1][1] += y

            for i in range(-1, -10, -1):
                H = P[i]
                T = P[i-1]

                dx = H[0] - T[0]
                dy = H[1] - T[1]

                if abs(dx) > 1 or abs(dy) > 1:
                    if dx == 0:
                        T[1] += 1 if dy > 0 else -1
                    elif dy == 0:
                        T[0] += 1 if dx > 0 else -1
                    else:
                        T[0] += 1 if dx > 0 else -1
                        T[1] += 1 if dy > 0 else -1

            VISITEDS.add(tuple(P[0]))
    return len(VISITEDS)


f = open('input.txt') # 6057
print(part_1(f))
f = open('input.txt') # 2514
print(part_2(f))