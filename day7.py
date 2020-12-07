import re
from aoc import read_file, timer


def parse_input():
    bag = re.compile(r'(\d+) (.+)')
    data = read_file(7)
    for line in data:
        bags = line.strip('.').split(' contain ')
        inner_bags = bags[1].split(', ')
        outer_bag = bags[0].rstrip('s')
        inner_bags = [(int(m.group(1)), m.group(2).rstrip('s')) for m in [bag.match(x) for x in inner_bags if bag.match(x)]]
        yield outer_bag, inner_bags

def check_bag_contains(bag, all_bags, contains=set()):
    for out, inner in all_bags:
        if list(filter(lambda x : x[1] == bag, inner)):
            contains.add(out)
            check_bag_contains(out, all_bags, contains)
    return contains

def get_bag_count(bag, all_bags, count=0):
    for out, inner in all_bags:
        if out != bag: continue
        count += sum([b[0] + (b[0] * get_bag_count(b[1], all_bags)) for b in inner])
    return count

@timer
def part1(data):
    return len(check_bag_contains('shiny gold bag', data))

@timer
def part2(data):
    return get_bag_count('shiny gold bag', data)

if __name__ == "__main__":
    data = list(parse_input())
    print(part1(data))

    print(part2(data))
