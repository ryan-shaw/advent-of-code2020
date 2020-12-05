from math import ceil
from aoc import read_file, timerc

def halve(_input, row_range, t='F', b='B'):
    c = _input.pop(0)
    diff = ceil((row_range[1] - row_range[0]) / 2) 
    if c == t:
        row_range[1] = row_range[1] - diff
    elif c == b:
        row_range[0] = row_range[0] + diff
    if not _input:
        assert row_range[0] == row_range[1]
        return row_range[0]
    return halve(_input, row_range, t=t, b=b)

def part1(data):
    for row in data:
        r = halve([c for c in row[:-3]], [0, 127])
        c = halve([c for c in row[-3:]], [0, 7], t='L', b='R')
        yield (r * 8) + c

if __name__ == "__main__":
    data = read_file(5)

    with timerc():
        res = list(part1(data))
        print(max(res))
    
    with timerc():
        [print(item + 1) if item + 2 in res and item + 1 not in res else None for item in res]