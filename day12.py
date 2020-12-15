from aoc import timer, read_file
from math import sin, cos

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def part1(data):
    FACING = EAST
    POS_X = 0
    POS_Y = 0
    for direction, count in data:
        if direction == 'F':
            if FACING == EAST: POS_X += count
            elif FACING == WEST: POS_X -= count
            elif FACING == NORTH: POS_Y += count
            elif FACING == SOUTH: POS_Y -= count
        elif direction == 'R':
            FACING = (FACING + count // 90) % 4
        elif direction == 'L':
            FACING = (FACING + -count // 90) % 4
        elif direction == 'N':
            POS_Y += count
        elif direction == 'E':
            POS_X += count
        elif direction == 'S':
            POS_Y -= count
        elif direction == 'W':
            POS_X -= count
        else:
            raise Exception('invalid direction')
    print(abs(POS_X) + abs(POS_Y))

def part2(data):
    WAYPOINT_X_DELTA = 10
    WAYPOINT_Y_DELTA = 1
    FACING = EAST
    POS_X = 0
    POS_Y = 0
    for direction, count in data:
        if direction == 'F':
            POS_X += (count * WAYPOINT_X_DELTA)
            POS_Y += (count * WAYPOINT_Y_DELTA)
        elif direction == 'R':
            for _ in range(count // 90):
                WAYPOINT_X_DELTA, WAYPOINT_Y_DELTA = (WAYPOINT_Y_DELTA, -WAYPOINT_X_DELTA)
        elif direction == 'L':
            for _ in range((count // 90)):
                WAYPOINT_X_DELTA, WAYPOINT_Y_DELTA = (-WAYPOINT_Y_DELTA, WAYPOINT_X_DELTA)
        elif direction == 'N':
            WAYPOINT_Y_DELTA += count
        elif direction == 'E':
            WAYPOINT_X_DELTA += count
        elif direction == 'S':
            WAYPOINT_Y_DELTA -= count
        elif direction == 'W':
            WAYPOINT_X_DELTA -= count
        else:
            raise Exception('invalid direction')
        print(f"{direction}{count} {FACING=}, {POS_X=}, {POS_Y=},  {WAYPOINT_X_DELTA=}, {WAYPOINT_Y_DELTA=}, {count=}")
    print(POS_X, POS_Y)
    print(abs(POS_X) + abs(POS_Y))


if __name__ == "__main__":
    data = read_file(12)
    data = [(line[0], int(line[1:])) for line in data]
    part1(data)
    part2(data)

# south = 2
# rotate -270 (-3) so we should get 3

# 