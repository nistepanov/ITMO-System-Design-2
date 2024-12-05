from random import randint

from entities.wall import Wall
from entities.mob import Mob
from entities.user import User
from entities.item import Item

from map.map import GameMap

from algorithms.simple_algo import SimpleAlgo


class MapGenerator:
    def __init__(self, window, rows, cloumns, start_x, start_y, bl_size):
        self.start_x = start_x
        self.start_y = start_y
        self.window = window
        self.bl_size = bl_size
        self.grid = []
        for i in range(rows):
            self.grid.append([])
            for j in range(cloumns):
                if i == 0 or j == 0 or i == rows - 1 or j == cloumns - 1:
                    self.grid[i].append('#')
                else:
                    self.grid[i].append('.')

    def generate_random_walls(self):
        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                if cell != ".":
                    continue
                if randint(0, 5) == 0:
                    self.grid[ry][rx] = '#'

    def generate_random_enemies(self):
        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                if cell != ".":
                    continue
                if randint(0, 20) == 0:
                    self.grid[ry][rx] = 'M'

    def generate_random_items(self):
        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                if cell != ".":
                    continue
                if randint(0, 20) == 0:
                    self.grid[ry][rx] = 'I'

    def generate_random_user(self):
        x = randint(1, len(self.grid)-1)
        y = randint(1, len(self.grid[0])-1)

        self.grid[x][y] = 'U'

    def create_map(self):
        self.window.tracer(0)
        simple_algo = SimpleAlgo()
        walls = []
        items = []
        mobs = []
        user = None
        self.generate_random_walls()
        self.generate_random_enemies()
        self.generate_random_items()
        self.generate_random_user()

        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                x = rx * self.bl_size - self.start_x
                y = ry * self.bl_size - self.start_y
                if cell == "#":
                    wall = Wall()
                    wall.goto(x, y)
                    walls.append((x, y))
                elif cell == "I":
                    item = Item()
                    item.goto(x, y)
                    items.append(item)
                elif cell == "U":
                    user = User(self.bl_size)
                    user.goto(x, y)
                elif cell == "M":
                    mob = Mob(simple_algo)
                    mob.goto(x, y)
                    mobs.append(mob)

                self.window.update()
        return GameMap(walls=walls, items=items, mobs=mobs, user=user, move_size=self.bl_size)

