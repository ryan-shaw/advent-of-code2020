from aoc import timer, read_file

SEAT_EMPTY = 'L'
SEAT_FULL = '#'
FLOOR = '.'

max_y = 0
max_x = 0

def print_seats(seats):
    """
    Seats are stored y, x
    """
    for row in seats:
        for seat in row:
            print(seat, end='')
        print()

def get_diaganols(y, x):
    for a_x in range(-min(x, y), min(max_x, max_y)):
        print(a_x, (y+a_x, x +a_x))
    
    for a_x in range(max(max_x - x, max_y - y), 0, -1):
        print(a_x, (y+a_x, x +a_x))

def check_adjacent(y, x, data):
    adj = 0
    for a_y in range(max(y-1, 0), min(y+2, max_y)):
        for a_x in range(max(x-1, 0), min(x+2, max_x)):
            if a_y == y and a_x == x: continue
            if data[a_y][a_x] == SEAT_FULL:
                adj +=1 

    get_diaganols(y, x)

    
    return adj

def count_seats(seats):
    count = 0
    for row in seats:
        for val in row:
            if val == SEAT_FULL:
                count += 1
    return count

@timer
def iterate_seats(seats):
    i = 0
    while True:
        modify = {SEAT_EMPTY: [], SEAT_FULL: []}
        for y, row in enumerate(seats):
            for x, col in enumerate(row):
                if col == SEAT_EMPTY:
                    adj = check_adjacent(y, x, seats)
                    if adj == 0:
                        modify[SEAT_FULL].append([y, x])
                elif col == SEAT_FULL:
                    adj = check_adjacent(y, x, seats)
                    if adj >= 4:
                        modify[SEAT_EMPTY].append([y, x])
        for y, x in modify[SEAT_EMPTY]:
            seats[y][x] = SEAT_EMPTY
        for y, x in modify[SEAT_FULL]:
            seats[y][x] = SEAT_FULL
        if not modify[SEAT_FULL] and not modify[SEAT_EMPTY]:
            print(i)
            return seats
        i += 1

if __name__ == "__main__":
    seats = read_file(11)
    max_y = len(seats)
    max_x = len(seats[0])
    for key, line in enumerate(seats):
        seats[key] = [x for x in line]
    
    # print_seats(seats)
    # iterate_seats(seats)
    # # print(check_adjacent(0, 3, seats))
    # print_seats(seats)
    # print(count_seats(seats))
    print(get_diaganols(3, 2))
