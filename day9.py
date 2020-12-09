from os import read
from aoc import timer, read_file
from itertools import combinations

preamble_length = 25

@timer
def part1(data):
    for idx in range(preamble_length, len(data) - 1):
        num = data[idx]
        preamble = [sum(x) for x in combinations(data[idx - preamble_length:idx], r=2)]
        if num not in preamble:
            return num

@timer
def part2(data, m):
    data = [d for d in data if d < m] # discard all above
    for x in range(len(data)):
        value = 0
        for y in range(x, len(data)):
            value += data[y]
            if value == m:
                return min(data[x:y]) + max(data[x:y])


if __name__ == "__main__":
    data = read_file(9, cast=int)
    res = part1(data)
    print(res)
    print(part2(data, res))
