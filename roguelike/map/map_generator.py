import turtle
from random import choice, randint

from roguelike.algorithms.simple_algo import SimpleAlgo
from roguelike.entities.artifact import Shield, Weapon
from roguelike.entities.mob import Mob
from roguelike.entities.user import User
from roguelike.entities.wall import Wall
from roguelike.map.map import GameMap


class MapGeneratorException(Exception):
    """Exception raised when some required game elems are None."""

    pass


class MapGenerator:
    """MapGenerator logic."""

    def __init__(
        self,
        window: turtle.TurtleScreen,
        rows: int,
        columns: int,
        start_x: int,
        start_y: int,
        bl_size: int,
    ) -> None:
        self.window = window
        self.start_x = start_x
        self.start_y = start_y
        self.bl_size = bl_size
        self.grid: list = []
        for i in range(rows):
            self.grid.append([])
            for j in range(columns):
                if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
                    self.grid[i].append('#')
                else:
                    self.grid[i].append('.')

    def generate_random_walls(self) -> None:
        """generate_random_walls logic.

        Returns:
            None: Description of return value
        """
        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                if cell != '.':
                    continue
                if randint(0, 5) == 0:
                    self.grid[ry][rx] = '#'

    def generate_random_enemies(self) -> None:
        """generate_random_enemies logic.

        Returns:
            None: Description of return value
        """
        is_enemies_generated = False
        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                if cell != '.':
                    continue
                if randint(0, 20) == 0:
                    self.grid[ry][rx] = 'M'
                    is_enemies_generated = True
        # at least one mob should be generated
        if not is_enemies_generated:
            self.grid[1][1] = 'M'  # improve in the future

    def generate_random_items(self) -> None:
        """generate_random_items logic.

        Returns:
            None: Description of return value
        """
        is_item_generated = False
        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                if cell != '.':
                    continue
                if randint(0, 40) == 0:
                    self.grid[ry][rx] = 'W'
                    is_item_generated = True
                if randint(0, 40) == 0:
                    self.grid[ry][rx] = 'S'
                    is_item_generated = True
        # at least one item should be generated
        if not is_item_generated:
            self.grid[2][2] = choice(['W', 'T'])  # improve in the future

    def generate_random_user(self) -> None:
        """generate_random_user logic.

        Returns:
            None: Description of return value
        """
        x = randint(1, len(self.grid) - 1)
        y = randint(1, len(self.grid[0]) - 1)
        self.grid[x][y] = 'U'

    def create_map(self, skip_generate: bool = False) -> GameMap:
        """create_map logic.

        Returns:
            GameMap: Description of return value
        """
        self.window.tracer(0)
        simple_algo = SimpleAlgo()
        walls: list[tuple[int, int]] = []
        item: Weapon | Shield
        items: list[Weapon | Shield] = []
        mobs: list[Mob] = []
        user: User | None = None
        if not skip_generate:
            self.generate_random_walls()
            self.generate_random_enemies()
            self.generate_random_items()
            self.generate_random_user()

        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                x = rx * self.bl_size - self.start_x
                y = ry * self.bl_size - self.start_y
                match cell:
                    case '#':
                        wall = Wall()
                        wall.goto(x, y)
                        walls.append((x, y))
                    case 'W':
                        item = Weapon(randint(0, 10))
                        item.goto(x, y)
                        items.append(item)
                    case 'S':
                        item = Shield(randint(0, 10))
                        item.goto(x, y)
                        items.append(item)
                    case 'U':
                        user = User(self.bl_size)
                        user.goto(x, y)
                    case 'M':
                        mob = Mob(simple_algo)
                        mob.goto(x, y)
                        mobs.append(mob)
                self.window.update()
        if not all([walls, items, mobs]) or user is None:
            raise MapGeneratorException
        print(walls, items, mobs)
        return GameMap(walls=walls, items=items, mobs=mobs, user_=user, move_size=self.bl_size)
