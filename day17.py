import itertools
from collections import defaultdict
from aoc import timer, read_file

class Space(object):

    def __init__(self, data):
        self.min_x = 0
        self.min_y = 0
        self.min_z = 0
        self.max_x = 8
        self.max_y = 7
        self.max_z = 0
        self.space = defaultdict(lambda: '.')
        for y, row in enumerate(data):
            for x, val in enumerate(row):
                self.space[(x, y, 0)] = val

    def get_neighbours(self, x, y, z):
        neighbours = list(itertools.product(range(-1, 2), repeat=3))
        return [(nx+x, ny+y, nz+z) for (nx, ny, nz) in neighbours if (nx+x, ny+y, nz+z) != (x, y, z) ]

    def display(self):
        for z in list(range(self.min_z, self.max_z + 1)):
            print(f"{z=}")
            for y in list(range(self.min_y, self.max_y + 1)):
                for x in list(range(self.min_x, self.max_x + 1)):
                    print(self.space[x, y, z], end='')
                print()
            print()

    def next_cell_value(self, position):
        neighbours = self.get_neighbours(*position)
        cube = self.space[position]
        count_active = sum(1 if self.space.get(ncube) == '#' else 0 for ncube in neighbours)
        if cube == '#' and count_active in [2,3]:
            return '#'
        elif cube == '.' and count_active == 3:
            return '#'
        return '.'

    def iterate(self):
        updates = {}
        
        locations = ([(x,y,z) 
            for z in list(range(self.min_z - 1, self.max_z + 2))
            for y in list(range(self.min_y - 1, self.max_y + 2))
            for x in list(range(self.min_x - 1, self.max_x + 2))
        ])
        for (x, y, z) in locations:
            updates[(x, y, z)] = self.next_cell_value((x, y, z))
        
        self.min_x -= 1
        self.min_y -= 1
        self.min_z -= 1
        self.max_x += 1
        self.max_y += 1
        self.max_z += 1
        self.space.update(updates)

@timer
def part1(data):
    s = Space(data)
    # s.display()

    for _ in range(6):
        s.iterate()
        # s.display()

    
    return (len([pos for pos, val in s.space.items() if val == '#']))
    

if __name__ == "__main__":
    data = read_file(17)
    print(part1(data))