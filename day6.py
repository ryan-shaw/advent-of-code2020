from aoc import read_file

def part1(data):
    for x in data:
        s = set()
        [s.update(t) for t in x]
        yield len(s)

if __name__ == "__main__":
    data = []
    tmp = []
    with open('./inputs/input06') as f:
        for line in [x.strip() for x in f.readlines()]:
            if line == '':
                data.append(tmp)
                tmp = []
            else:
                tmp.append(set([c for c in line]))
        data.append(tmp)

    print(sum((part1(data))))

    print(sum([len(set.intersection(*x)) for x in data]))