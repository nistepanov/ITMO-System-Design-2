# roguelike.map package

## Submodules

## roguelike.map.map module

### *class* roguelike.map.map.GameMap(walls: list[tuple[int, int]], mobs: list[[Mob](roguelike.entities.md#roguelike.entities.mob.Mob)], items: list[[Weapon](roguelike.entities.md#roguelike.entities.artifact.Weapon) | [Shield](roguelike.entities.md#roguelike.entities.artifact.Shield)], user_: [User](roguelike.entities.md#roguelike.entities.user.User), move_size: int)

Базовые классы: `object`

GameMap logic.

#### check_walls(x: float, y: float) → bool

check_walls logic.

* **Параметры:**
  * **x** (*float*) – Coord of x.
  * **y** (*float*) – Coord of y.
* **Результат:**
  Is coordinates not covered by walls.
* **Тип результата:**
  bool

## roguelike.map.map_generator module

### *class* roguelike.map.map_generator.MapGenerator(window: TurtleScreen, rows: int, columns: int, start_x: int, start_y: int, bl_size: int)

Базовые классы: `object`

MapGenerator logic.

#### create_map() → [GameMap](#roguelike.map.map.GameMap)

create_map logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  [GameMap](#roguelike.map.map.GameMap)

#### generate_random_enemies() → None

generate_random_enemies logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_random_items() → None

generate_random_items logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_random_user() → None

generate_random_user logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### generate_random_walls() → None

generate_random_walls logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

### *exception* roguelike.map.map_generator.MapGeneratorException

Базовые классы: `Exception`

Exception raised when some required game elems are None.

## Module contents
