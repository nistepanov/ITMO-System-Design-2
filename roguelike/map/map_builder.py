# mypy: disable-error-code="assignment, arg-type, attr-defined, index, var-annotated"
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
from roguelike.mob_factory.passive_mobs_factory import PassiveMobsFactory


class MapBuilderException(Exception):
    """Exception raised when some required game elems are None."""

    pass


class MapBuilder:
    """MapBuilder logic for generating or loading maps."""

    _USER_LEVEL = 1
    _USER_HEALTH = 10
    _USER_DAMAGE = 1

    def __init__(self, window: turtle.TurtleScreen) -> None:
        self.window = window
        self.rows = 10
        self.columns = 10
        self.start_x = 0
        self.start_y = 0
        self.bl_size = 40
        self.grid: list[int] = []
        self.load_from_file = False
        self.file_path = None
        self.mob_factories = [PassiveMobsFactory(), AggressiveMobsFactory(), CowardMobsFactory()]
        self.inventory_shift = -420
        self.active_items_shift = -350
        self.stats_shift = -280
        self.default_font = ('Arial', 12, 'normal')
        self.data_font = ('Arial', 40, 'normal')
        self.experience_slot = None
        self.weapon_slot = None
        self.shield_slot = None

    def set_map_size(self, rows: int, columns: int) -> 'MapBuilder':
        """Set the size of the map."""
        self.rows = rows
        self.columns = columns
        return self

    def set_start_position(self, start_x: int, start_y: int) -> 'MapBuilder':
        """Set the starting position of the map."""
        self.start_x = start_x
        self.start_y = start_y
        return self

    def set_block_size(self, block_size: int) -> 'MapBuilder':
        """Set the size of each block."""
        self.bl_size = block_size
        return self

    def load_map_from_file(self, file_path: str | None) -> 'MapBuilder':
        """Set the map to be loaded from a file."""
        if file_path is not None:
            self.load_from_file = True
            self.file_path = file_path
            return self
        raise MapBuilderException('MapBuilder: file_path is None')

    def build(self) -> GameMap:
        """Construct the map based on the current settings."""
        if self.load_from_file:
            self._load_map_from_file()
        else:
            self._generate_map()

        return self._create_game_map()

    def _load_map_from_file(self) -> None:
        """Load map from a file."""
        if not self.file_path:
            raise MapBuilderException('File path must be provided to load the map.')
        self.grid = []
        with open(self.file_path) as file:
            for line in file:
                self.grid.append(list(line.strip()))

    def _generate_map(self) -> None:
        """Generate a new random map."""
        self.grid = []
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.columns):
                if i == 0 or j == 0 or i == self.rows - 1 or j == self.columns - 1:
                    self.grid[i].append('#')
                else:
                    self.grid[i].append('.')

        self._generate_random_walls()
        self._generate_random_enemies()
        self._generate_random_items()
        self._generate_random_user()

    def _generate_random_walls(self) -> None:
        """_generate_random_walls logic.

        Returns:
            None: Description of return value
        """
        for ry, row in enumerate(self.grid):
            for rx, cell in enumerate(row):
                if cell != '.':
                    continue
                if randint(0, 5) == 0:
                    self.grid[ry][rx] = '#'

    def _generate_random_enemies(self) -> None:
        """_generate_random_enemies logic.

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
        if not is_enemies_generated:
            self.grid[1][1] = 'M'

    def _generate_random_items(self) -> None:
        """_generate_random_items logic.

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
        if not is_item_generated:
            self.grid[2][2] = choice(['W', 'T'])

    def _generate_random_user(self) -> None:
        """_generate_random_user logic.

        Returns:
            None: Description of return value
        """
        x = randint(1, len(self.grid) - 2)
        y = randint(1, len(self.grid[0]) - 2)
        self.grid[x][y] = 'U'

    def _create_game_map(self) -> GameMap:
        """_create_game_map logic.

        Returns:
            GameMap: Description of return value
        """
        self.window.tracer(0)
        walls = []
        items = []
        mobs = []
        user = None
        inventory = self._generate_inventory()
        self._generate_stats()

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
                            health=MapBuilder._USER_HEALTH,
                            damage=MapBuilder._USER_DAMAGE,
                            level=MapBuilder._USER_LEVEL,
                        )
                        user.goto(x, y)
                    case 'M':
                        mob = self._get_mob()
                        mob.goto(x, y)
                        mobs.append(mob)
                self.window.update()
        if not all([walls, items, mobs]) or user is None or inventory is None:
            raise MapBuilderException('Failed to create map.')
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

    def _generate_inventory(self) -> Inventory:
        """_generate_inventory logic.

        Returns:
            Inventory: Description of return value
        """
        active_items = []
        active = Image('/active_items.gif')
        active.goto(-1 * self.bl_size - self.start_x, self.active_items_shift)
        symbols = ['q', 'w', 'e']
        for i in range(3):
            item = InventorySlot()
            item.goto(i * self.bl_size - self.start_x, self.active_items_shift)
            item.write(symbols[i], align='center', font=self.default_font)
            active_items.append(item)

        inventory = []
        backpack = Image('/backpack.gif')
        backpack.goto(-1 * self.bl_size - self.start_x, self.inventory_shift)
        for i in range(6):
            item = InventorySlot()
            item.goto(i * self.bl_size - self.start_x, self.inventory_shift)
            item.write(str(i + 1), align='center', font=self.default_font)
            inventory.append(item)

        return Inventory(inventory=inventory, active_items=active_items)

    def _generate_stats(self) -> None:
        """_generate_stats logic.

        Returns:
            None: Description of return value
        """
        level = Image('/level.gif')
        level.goto(-self.bl_size - self.start_x, self.stats_shift)
        self.experience_slot = TextObject()
        self.experience_slot.goto(-self.start_x, self.stats_shift - self.bl_size / 3)
        self.experience_slot.write(str(MapBuilder._USER_LEVEL), align='center', font=self.data_font)

        active = Image('/weapon.gif')
        active.goto(self.bl_size - self.start_x, self.stats_shift)
        self.weapon_slot = TextObject()
        self.weapon_slot.goto(2 * self.bl_size - self.start_x, self.stats_shift - self.bl_size / 3)
        self.weapon_slot.write(str(MapBuilder._USER_DAMAGE), align='center', font=self.data_font)

        shield = Image('/shield.gif')
        shield.goto(3 * self.bl_size - self.start_x, self.stats_shift)
        self.shield_slot = TextObject()
        self.shield_slot.goto(4 * self.bl_size - self.start_x, self.stats_shift - self.bl_size / 3)
        self.shield_slot.write(str(MapBuilder._USER_HEALTH), align='center', font=self.data_font)

    def _get_mob(self) -> Mob:
        """Creates a new random mob using one of the mob factories."""
        return self.mob_factories[randint(0, len(self.mob_factories) - 1)].create_random_mob()
