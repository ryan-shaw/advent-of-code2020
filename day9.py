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

if __name__ == "__main__":
    data = read_file(9, cast=int)
    part1(data)
