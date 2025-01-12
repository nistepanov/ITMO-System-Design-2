# roguelike.state package

## Submodules

## roguelike.state.bravery_state module

### *class* roguelike.state.bravery_state.BraveryState

Базовые классы: [`MobState`](#roguelike.state.mob_state.MobState)

BraveryState logic.

#### *static* move(entity: Any, game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** – mob.Mob
  * **game_map** – map.GameMap
* **Результат:**
  Description of return value
* **Тип результата:**
  tuple[float, float] | None

## roguelike.state.default_state module

### *class* roguelike.state.default_state.DefaultState

Базовые классы: [`MobState`](#roguelike.state.mob_state.MobState)

DefaultState logic.

#### *static* move(entity: Any, game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** – mob.Mob
  * **game_map** – map.GameMap
* **Результат:**
  Description of return value
* **Тип результата:**
  tuple[float, float] | None

### roguelike.state.default_state.check_is_someone_near(entity: Any, game_map: Any) → bool

check_is_someone_near logic.

* **Параметры:**
  * **entity** – mob.Mob
  * **game_map** – map.GameMap
* **Результат:**
  Description of return value
* **Тип результата:**
  bool

## roguelike.state.mob_state module

### *class* roguelike.state.mob_state.MobState

Базовые классы: `object`

MobState logic.

#### *static* move(entity: Any, game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## roguelike.state.panic_state module

### *class* roguelike.state.panic_state.PanicState

Базовые классы: [`MobState`](#roguelike.state.mob_state.MobState)

DefaultState logic.

#### *static* move(entity: Any, game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** – mob.Mob
  * **game_map** – map.GameMap
* **Результат:**
  Description of return value
* **Тип результата:**
  tuple[float, float] | None

## Module contents
