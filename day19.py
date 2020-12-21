from aoc import timer, read_file

def solve(rules, rule, _input):
    if rule.isalpha():
        c = _input.pop(0)
        return c == rule

    for sub_rules in rules[rule]:
        _input_copy = _input.copy()
        x = all([solve(rules, rule1, _input_copy) for rule1 in sub_rules])
        if x:
            _input.clear()
            [_input.append(i) for i in _input_copy]
            if rule == '0' and not _input:
                return True
            elif rule == '0': 
                return False
            return x

def parse_input(data):
    graph = {}
    inputs = []
    for line in data:
        if not line: continue
        if ':' in line:
            key = line[:line.index(':')]
            graph[key] = []
            for sub in [x.strip() for x in line[line.index(':') + 2:].split('|')]:
                graph[key].append([ss.replace('"', '') for ss in sub.split(' ')])
        else:
            inputs.append([c for c in line.strip()])

    return graph, inputs

if __name__ == "__main__":
    data = read_file(19)
    data, inputs  = parse_input(data)
    out = [solve(data, '0', _in) for _in in inputs]
    print(out.count(True))
