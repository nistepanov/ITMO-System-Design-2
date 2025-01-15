# roguelike.map package

## Submodules

## roguelike.map.map module

### *class* roguelike.map.map.GameMap(walls: list[tuple[int, int]], mobs: list[[Mob](roguelike.entities.md#roguelike.entities.mob.Mob)], items: list[[Weapon](roguelike.entities.md#roguelike.entities.artifact.Weapon) | [Shield](roguelike.entities.md#roguelike.entities.artifact.Shield)], user_: [User](roguelike.entities.md#roguelike.entities.user.User), move_size: int, inventory: Inventory, experience_slot: TextObject | None, weapon_slot: TextObject | None, shield_slot: TextObject | None)

Базовые классы: `object`

GameMap logic.

#### check_walls(x: float, y: float) → bool

Checks if the coordinate is not a wall.

* **Параметры:**
  * **x** (*float*) – Coord of x.
  * **y** (*float*) – Coord of y.
* **Результат:**
  Is coordinates not covered by walls.
* **Тип результата:**
  bool

#### is_user(x: float, y: float) → bool

Checks if there is user in given coordinates.

* **Параметры:**
  * **x** (*float*) – Coord of x.
  * **y** (*float*) – Coord of y.
* **Результат:**
  Is coordinates covered by users.
* **Тип результата:**
  bool

## roguelike.map.map_generator module

### *class* roguelike.map.map_generator.MapGenerator(window: TurtleScreen, rows: int, columns: int, start_x: int, start_y: int, bl_size: int)

Базовые классы: `object`

MapGenerator logic.

#### create_map(skip_generate: bool = False) → [GameMap](#roguelike.map.map.GameMap)

Base function of map creation.

* **Результат:**
  Description of return value
* **Тип результата:**
  [GameMap](#roguelike.map.map.GameMap)

#### generate_inventory() → Inventory

generate_inventory logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_random_enemies() → None

Puts enemies into random spots.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_random_items() → None

Puts items into random spots.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_random_user() → None

Puts user into random spot.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_random_walls() → None

Generates walls.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_stats() → None

Calculates stats of user abilities and perks.

#### get_mob() → [Mob](roguelike.entities.md#roguelike.entities.mob.Mob)

Creates new mob.

* **Результат:**
  Description of return value
* **Тип результата:**
  [Mob](roguelike.entities.md#roguelike.entities.mob.Mob)

### *exception* roguelike.map.map_generator.MapGeneratorException

Базовые классы: `Exception`

Exception raised when some required game elems are None.

## Module contents
