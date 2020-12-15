import re
import itertools
import functools
from aoc import read_file, timer

memory = {}

TEST = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n')

TEST2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n')

MEM = re.compile(r'mem\[(\d+)\] = (\d+)')

def part1(data):
    mask = None
    one_mask = 0
    zero_mask = 0
    for line in data:
        if line.startswith('mask'):
            mask = line[line.index('=') + 2:]
            one_mask = 0
            zero_mask = 0
            for c in mask:
                one_mask <<= 1
                zero_mask <<= 1
                if c == '1':
                    one_mask |= 1
                elif c == '0':
                    zero_mask |= 1
        else:
            match = MEM.match(line)
            address, value = int(match.group(1)), int(match.group(2))
            masked_value = (value | one_mask) & (0b111111111111111111111111111111111111 ^ zero_mask)
            memory[address] = masked_value
        
def part2(data):
    mask = None
    one_mask = 0
    zero_mask = 0
    float_mask = 0
    float_offsets = []
    for line in data:
        if line.startswith('mask'):
            mask = line[line.index('=') + 2:]
            one_mask = 0
            zero_mask = 0
            float_mask = 0
            float_offset = 1
            float_offsets = []
            for c in mask:
                one_mask <<= 1
                zero_mask <<= 1
                float_mask <<= 1
                
                if c == '1':
                    one_mask |= 1
                elif c == '0':
                    zero_mask |= 1
                elif c == 'X':
                    float_mask |= 1
            for c in mask[::-1]:
                if c == 'X':
                    float_offsets.append(float_offset)
                    print(f"{float_offset=:>036b} {float_offset}")
                float_offset <<= 1
        else:
            combinations = \
            [
                functools.reduce(lambda a, b : a | b, x)
                for x in list(itertools.product(*((c, 0) for c in float_offsets)))
            ]
            match = MEM.match(line)
            address, value = int(match.group(1)), int(match.group(2))
            address |= one_mask
            address &= (0b111111111111111111111111111111111111 ^ float_mask)
            for c in combinations:
                memory[address | c] = value

if __name__ == "__main__":
    data = read_file(14)

    # part1(TEST)
    # part1(data)
    # part2(TEST2)
    part2(data)
    
    print(sum(memory.values()))
