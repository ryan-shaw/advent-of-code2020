from collections import defaultdict

memory = defaultdict(list)
# TEST = "0,3,6"
INPUT = "7,14,0,17,11,1,2"

if __name__ == "__main__":
    starting = [int(c) for c in INPUT.split(',')]
    turn = 1
    last_num = None
    for n in starting:
        memory[n].append(turn)
        turn += 1
        last_num = n

    iterations = 30000000

    for n in range(turn, iterations + 1):
        if len(memory[last_num]) == 1:
            last_num = 0
        else:
            last_num = memory[last_num][-1] - memory[last_num][-2]
        memory[last_num].append(turn) 
        turn += 1
    print(last_num)
