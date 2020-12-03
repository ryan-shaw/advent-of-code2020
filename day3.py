from aoc import timer, read_file

def tree_check(data, xdelta, ydelta):
    cols = len(data[0])
    y = 0
    x = 0
    while y < len(data) - 1:
        x += xdelta
        y += ydelta
        if data[y][(x % cols)] == '#':
            yield True

@timer
def part1(data):
    return tree_check(data, 3, 1)

@timer
def part2(data):
    return len(list(tree_check(data, 1, 1))) \
        * len(list(tree_check(data, 3, 1))) \
        * len(list(tree_check(data, 5, 1))) \
        * len(list(tree_check(data, 7, 1))) \
        * len(list(tree_check(data, 1, 2)))

if __name__ == "__main__":
    data = read_file(3)
    result = len(list(part1(data)))
    print(result)
    result = part2(data)
    print(result)
