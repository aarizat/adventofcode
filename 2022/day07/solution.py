from pathlib import Path
from collections import defaultdict


def part_1(file) -> int:
    dirs = defaultdict(int)
    cwd = Path('/')
    for line in file.read().splitlines():
        match line.split():
            case ['$', 'cd', folder]:
                cwd = cwd / folder
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                for path in [cwd, *cwd.parents]:
                    dirs[path] += int(size)

    return sum(size for size in dirs.values() if size <= 100000)


def part_2(file) -> int:
    dirs = defaultdict(int)
    cwd = Path('/')
    for line in file.read().splitlines():
        match line.split():
            case ['$', 'cd', folder]:
                cwd = cwd / folder
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                for path in [cwd, *cwd.parents]:
                    dirs[path] += int(size)
    return min(size for size in dirs.values() if size >= 30000000 - (70000000-dirs[Path("/")]))


f = open('input.txt')
print(part_1(f))
f = open('input.txt')
print(part_2(f))