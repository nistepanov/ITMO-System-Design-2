import turtle
from random import choice, randint

from roguelike.entities.artifact import Shield, Weapon
from roguelike.entities.image import Image
from roguelike.entities.inventory_slot import InventorySlot
from roguelike.entities.mob import Mob
from roguelike.entities.text_object import TextObject
from roguelike.entities.user import User
from roguelike.entities.wall import Wall
from roguelike.inventory.inventory import Inventory
from roguelike.map.map import GameMap
from roguelike.mob_factory.agressive_mobs_factory import AggressiveMobsFactory
from roguelike.mob_factory.cowards_mobs_factory import CowardMobsFactory
from roguelike.mob_factory.mob_factory import MobFactory
from roguelike.mob_factory.passive_mobs_factory import PassiveMobsFactory


class MapGeneratorException(Exception):
    """Exception raised when some required game elems are None."""

    pass


class MapGenerator:
    """MapGenerator logic."""

    _USER_LEVEL = 1
    _USER_HEALTH = 10
    _USER_DAMAGE = 1

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
        self.inventory_shift = -420
        self.active_items_shift = -350
        self.stats_shift = -280
        self.default_font = ('Arial', 12, 'normal')
        self.data_font = ('Arial', 40, 'normal')
        self.experience_slot: TextObject | None = None
        self.weapon_slot: TextObject | None = None
        self.shield_slot: TextObject | None = None
        self.mob_factories: list[MobFactory] = [PassiveMobsFactory(), AggressiveMobsFactory(), CowardMobsFactory()]

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
                if randint(0, 20) == 0:
                    self.grid[ry][rx] = 'W'
                    is_item_generated = True
                if randint(0, 20) == 0:
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

    def generate_inventory(self) -> Inventory:
        """generate_inventory logic.

        Returns:
            None: Description of return value
        """
        active_items = []
        active = Image('/active_items.gif')
        active.goto(-1 * self.bl_size - self.start_x, self.active_items_shift)
        symbols = ['q', 'w', 'e']
        for i in range(0, 3):
            item = InventorySlot()
            item.goto(i * self.bl_size - self.start_x, self.active_items_shift)
            item.write(symbols[i], align='center', font=self.default_font)
            active_items.append(item)

        inventory = []
        backpack = Image('/backpack.gif')
        backpack.goto(-1 * self.bl_size - self.start_x, self.inventory_shift)
        for i in range(0, 6):
            item = InventorySlot()
            item.goto(i * self.bl_size - self.start_x, self.inventory_shift)
            item.write(str(i + 1), align='center', font=self.default_font)
            inventory.append(item)

        return Inventory(inventory=inventory, active_items=active_items)

    def generate_stats(self) -> None:
        """generate_stats logic."""
        level = Image('/level.gif')
        level.goto(-self.bl_size - self.start_x, self.stats_shift)
        self.experience_slot = TextObject()
        self.experience_slot.goto(-self.start_x, self.stats_shift - self.bl_size / 3)
        self.experience_slot.write(str(MapGenerator._USER_LEVEL), align='center', font=self.data_font)

        active = Image('/weapon.gif')
        active.goto(self.bl_size - self.start_x, self.stats_shift)
        self.weapon_slot = TextObject()
        self.weapon_slot.goto(2 * self.bl_size - self.start_x, self.stats_shift - self.bl_size / 3)
        self.weapon_slot.write(str(MapGenerator._USER_DAMAGE), True, align='center', font=self.data_font)

        level = Image('/shield.gif')
        level.goto(3 * self.bl_size - self.start_x, self.stats_shift)
        self.shield_slot = TextObject()
        self.shield_slot.goto(4 * self.bl_size - self.start_x, self.stats_shift - self.bl_size / 3)
        self.shield_slot.write(MapGenerator._USER_HEALTH, align='center', font=self.data_font)

    def get_mob(self) -> Mob:
        """get_mob logic.

        Returns:
            Mob: Description of return value
        """
        return self.mob_factories[randint(0, 2)].create_random_mob()

    def create_map(self, skip_generate: bool = False) -> GameMap:
        """create_map logic.

        Returns:
            GameMap: Description of return value
        """
        self.window.tracer(0)
        walls: list[tuple[int, int]] = []
        item: Weapon | Shield
        items: list[Weapon | Shield] = []
        mobs: list[Mob] = []
        user: User | None = None
        inventory: Inventory | None = None

        if not skip_generate:
            self.generate_random_walls()
            self.generate_random_enemies()
            self.generate_random_items()
            self.generate_random_user()
            self.generate_stats()
            inventory = self.generate_inventory()

        if inventory is None:
            raise MapGeneratorException

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
                        item = Weapon(1)
                        item.goto(x, y)
                        items.append(item)
                    case 'S':
                        item = Shield(1)
                        item.goto(x, y)
                        items.append(item)
                    case 'U':
                        user = User(
                            inventory=inventory,
                            health=MapGenerator._USER_HEALTH,
                            damage=MapGenerator._USER_DAMAGE,
                            level=MapGenerator._USER_LEVEL,
                        )
                        user.goto(x, y)
                    case 'M':
                        mob = self.get_mob()
                        mob.goto(x, y)
                        mobs.append(mob)
                self.window.update()
        if not all([walls, items, mobs]) or user is None or inventory is None:
            raise MapGeneratorException
        return GameMap(
            walls=walls,
            items=items,
            mobs=mobs,
            user_=user,
            move_size=self.bl_size,
            inventory=inventory,
            experience_slot=self.experience_slot,
            weapon_slot=self.weapon_slot,
            shield_slot=self.shield_slot,
        )
