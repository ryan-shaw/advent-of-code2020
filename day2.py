import re
from aoc import timer, read_file

def policy_check(data):
    pattern = re.compile(r'(\d+)\-(\d+) ([a-z]): ([a-z]+)')
    for entry in data:
        m = pattern.match(entry)
        _min, _max, policy, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        count = password.count(policy)
        if not (_min > count or count > _max):
            yield password

def new_policy_check(data):
    pattern = re.compile(r'(\d+)\-(\d+) ([a-z]): ([a-z]+)')
    for entry in data:
        m = pattern.match(entry)
        pos1, pos2, policy, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
        if (password[pos1-1] == policy) != (password[pos2-1] == policy):
            yield password

@timer
def part1(data):
    result = len(list(policy_check(data)))
    print('Part 1 result:', result)

@timer
def part2(data):
    result = len(list(new_policy_check(data)))
    print('Part 2 result', result)

if __name__ == "__main__":
    data = read_file(2)
    part1(data)
    part2(data)
