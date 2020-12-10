from aoc import timer, read_file
from itertools import combinations, permutations
import math

@timer
def part1(data):
    data = sorted(data)
    data = [0] + data + [data[-1] + 3]
    diff = [data[x + 1] - data[x] for x in range(len(data) - 1)]
    print(diff.count(1) + (diff.count(3) * 3))
    return (diff.count(1) + 1) * (diff.count(3) + 1)

if __name__ == "__main__":
    data = read_file(10, cast=int)
    print(part1(data))
