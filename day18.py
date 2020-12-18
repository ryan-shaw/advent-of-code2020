from aoc import timer, read_file
import math

def eval_exp(exp):
    stack = []
    out = []
    print(exp)
    for c in exp:
        if isinstance(c, int):
            out.append(c)
            if len(out) == 2:
                op = stack.pop()
                if op == '+':
                    out.append(out.pop() + out.pop())
                elif op == '*':
                    out.append(out.pop() * out.pop())
        elif c in ('+', '*'):
            stack.append(c)
    return out.pop()

def eval_mul(exp):
    exp = ''.join([str(x) for x in exp])
    return math.prod(eval(x) for x in exp.split('*'))

def solve(input, eval_func=eval_exp):
    out = []
    stack = []
    for c in input.replace(' ', ''):
        if c.isnumeric():
            out.append(int(c))
        elif c in ('*', '+'):
            out.append(c)
        elif c == '(':
            stack.append(out)
            out = []
        elif c == ')':
            val = eval_func(out)
            stack[-1].append(val)
            out = stack.pop()
    return eval_func(out)

@timer
def part1(data):
    return sum([solve(line, eval_exp) for line in data])

@timer
def part2(data):
    return sum([solve(line, eval_func=eval_mul) for line in data])

if __name__ == "__main__":
    data = read_file(18)
    # print(part1(data))
    # print(rpn('1 + ((3 + 3) * 2)'))
    # print(solve('2 * 3 + (4 * 5)'))
    # print(solve('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
    # print(solve('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
    # print(solve('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
    print(part1(data))

    # print(solve('1 + (2 * 3) + (4 * (5 + 6))', eval_func=eval_mul))
    # print(solve('2 * 3 + (4 * 5)', eval_func=eval_mul))
    # print(solve('5 + (8 * 3 + 9 + 3 * 4 * 3)', eval_func=eval_mul))
    # print(solve('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', eval_func=eval_mul))
    # print(solve('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', eval_func=eval_mul))

    print(part2(data))
