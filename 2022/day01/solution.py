import heapq


def part_1(file: str) -> int:
    with open(file, mode="r") as f:
        maximum = accum = 0
        for line in f:
            if line != '\n':
                accum += int(line)
            else:
                maximum =  max(accum, maximum)
                accum = 0
        return max(maximum, accum)


def part_2(file: str) -> int:
    with open(file, mode="r") as f:
        list_accum, accum = [], 0
        for line in f:
            if line == '\n':
                list_accum.append(accum)
                accum = 0
            else:
                accum += int(line)
        list_accum.append(accum)
    return sum(heapq.nlargest(3, list_accum))


print(part_1("input.txt")) # 68442
print(part_2("input.txt")) # 204837