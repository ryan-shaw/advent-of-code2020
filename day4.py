import re
from aoc import timer, read_file


def parse_passports(data):
    entry = {}
    for line in data:
        if not line: 
            yield entry
            entry = {}
            continue
        res = {key: value for (key, value) in [x.split(':') for x in line.split(' ')]}
        entry.update(res)
    yield entry

def check_fields(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if field not in passport:
            return False
    return True

def check_valid(passport):
    validators = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2010 <= int(x) <= 2030,
        'hgt': lambda x: 59 <= int(x[:-2]) <= 76 if 'in' in x else (150 <= int(x[:-2]) <= 193 if 'cm' in x else False),
        'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x),
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: re.match(r'^[0-9]{9}$', x),
    }
    for key, validator in validators.items():
        if key not in passport:
            return False
        if not validator(passport[key]):
            return False
    return True

@timer
def part1(data):
    passports = parse_passports(data)
    return sum([check_fields(passport) for passport in passports])

@timer
def part2(data):
    passports = parse_passports(data)
    return sum([check_valid(passport) for passport in passports])


if __name__ == "__main__":
    data = read_file(4, split='\n')
    print(part1(data))
    print(part2(data))
