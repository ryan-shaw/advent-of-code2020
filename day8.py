from aoc import timer, read_file

def parse_data(data):
    acc = 0
    addresses = set()
    address = 0
    while address < len(data):
        op, arg = data[address].split(' ')
        if address in addresses:
            raise Exception(f"infinte loop, acc = {acc}")
        addresses.add(address)
        if op == 'nop': 
            address += 1
            continue
        elif op == 'acc': 
            address += 1
            acc += int(arg)
        elif op == 'jmp': 
            address += int(arg)
            continue
    return acc

@timer
def brute(data):
    # brute force corruption until we succeed
    for address in range(len(data)):
        op, arg = data[address].split(' ')
        if op in ['nop', 'jmp']:
            new_data = list(data)
            new_data[address] = ('nop' if op == 'jmp' else 'jmp') + ' ' + arg
            try:
                print(parse_data(new_data))
                break
            except:
                pass

if __name__ == "__main__":
    data = read_file(8)
    try:
        print(parse_data(data))
    except Exception as e:
        print(e)

    print(brute(data))

