import re
from aoc import read_file, timer

memory = {}

def apply_mask(value, one_mask, zero_mask):
    return (value | one_mask) & zero_mask

def parse_data(data):
    for key, instruction in enumerate(data):
        if instruction.startswith('mask'):
            mask = instruction[instruction.index('=') + 2:]
            ones = int(b''.join([b'1' if x == '1' else b'0' for x in mask]), 2)
            zeroes = int(b''.join([b'0' if x == '0' else b'1' for x in mask]), 2)
            delta = 1
            r_mem = re.compile(r'mem\[(\d+)\] = (\d+)')
            while key + delta < len(data) and (match := r_mem.match(data[key + delta])) is not None:
                delta += 1
                address, value = int(match.group(1)), int(match.group(2))
                masked = apply_mask(value, ones, zeroes)
                memory[address] = masked

if __name__ == "__main__":
    data = read_file(14)
    # print(list(enumerate(data)))

    list(parse_data(data))
    print(sum(memory.values()))
