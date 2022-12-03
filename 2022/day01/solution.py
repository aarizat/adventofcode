import heapq


def part_1(file: str) -> int:
    with open(file, mode="r") as f:
        return max(
            sum(map(int, line.split()))
            for line in f.read().split('\n\n')
        )


def part_2(file: str) -> int:
    with open(file, mode="r") as f:
        list_accum = [
            sum(map(int, line.split()))
            for line in f.read().split('\n\n')
        ]
        return sum(heapq.nlargest(3,list_accum))


print(part_1("input.txt")) # 68442
print(part_2("input.txt")) # 204837