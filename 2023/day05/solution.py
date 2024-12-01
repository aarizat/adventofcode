def read_input(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip('\n')


