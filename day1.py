from aoc import timer, read_file
from math import prod
from itertools import combinations

@timer
def sum_prod(data, r=2):
    data = sorted(data)
    perms = combinations(data, r=r)
    for perm in perms:
        if sum(perm) == 2020:
            return prod(perm)

if __name__ == "__main__":
    data = read_file(1, cast=int)
    result = sum_prod(data)
    print("Part 1 result", result)
    result = sum_prod(data, r=3)
    print("Part 2 result", result)
