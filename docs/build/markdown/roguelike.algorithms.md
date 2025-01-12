# roguelike.algorithms package

## Submodules

## roguelike.algorithms.agressive_algo module

### *class* roguelike.algorithms.agressive_algo.AgressiveAlgo

Базовые классы: [`MobAlgorithm`](#roguelike.algorithms.mob_algorithm.MobAlgorithm)

SimpleAlgo logic.

#### move(entity: Any, game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## roguelike.algorithms.coward_algo module

### *class* roguelike.algorithms.coward_algo.CowardAlgo

Базовые классы: [`MobAlgorithm`](#roguelike.algorithms.mob_algorithm.MobAlgorithm)

SimpleAlgo logic.

#### move(entity: Any, game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## roguelike.algorithms.mob_algorithm module

### *class* roguelike.algorithms.mob_algorithm.MobAlgorithm

Базовые классы: `object`

MobAlgorithm logic.

#### *abstract* move(entity: Any, game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## roguelike.algorithms.mob_decorator module

### *class* roguelike.algorithms.mob_decorator.AbstractDecorator(confused_seconds: int, decoratee: [MobAlgorithm](#roguelike.algorithms.mob_algorithm.MobAlgorithm))

Базовые классы: [`MobAlgorithm`](#roguelike.algorithms.mob_algorithm.MobAlgorithm)

AbstractDecorator logic.

#### *abstract* move(entity: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob), game_map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap)) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## roguelike.algorithms.mob_decorator_confused module

### *class* roguelike.algorithms.mob_decorator_confused.ConfusedDecorator(confused_seconds: int, decoratee: [MobAlgorithm](#roguelike.algorithms.mob_algorithm.MobAlgorithm))

Базовые классы: [`AbstractDecorator`](#roguelike.algorithms.mob_decorator.AbstractDecorator)

SimpleAlgo logic.

#### move(entity: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob), game_map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap)) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_down(entity: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob), game_map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap)) → tuple[float, float] | None

shift_down logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_left(entity: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob), game_map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap)) → tuple[float, float] | None

shift_left logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_right(entity: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob), game_map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap)) → tuple[float, float] | None

shift_right logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_up(entity: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob), game_map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap)) → tuple[float, float] | None

shift_up logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## roguelike.algorithms.passive_algo module

### *class* roguelike.algorithms.passive_algo.PassiveAlgo

Базовые классы: [`MobAlgorithm`](#roguelike.algorithms.mob_algorithm.MobAlgorithm)

SimpleAlgo logic.

#### move(entity: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob), game_map: [GameMap](roguelike.map.md#roguelike.map.map.GameMap)) → tuple[float, float] | None

Move logic.

* **Параметры:**
  * **entity** ([*mob.Mob*](roguelike.entities.md#roguelike.entities.mob.Mob)) – Description of entity.
  * **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

## Module contents
