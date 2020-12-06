from aoc import read_file

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

    print(sum([len(set.union(*x)) for x in data]))

    print(sum([len(set.intersection(*x)) for x in data]))