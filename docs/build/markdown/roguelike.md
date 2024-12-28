# roguelike package

## Subpackages

* [roguelike.algorithms package](roguelike.algorithms.md)
  * [Submodules](roguelike.algorithms.md#submodules)
  * [roguelike.algorithms.mob_algorithm module](roguelike.algorithms.md#module-roguelike.algorithms.mob_algorithm)
    * [`MobAlgorithm`](roguelike.algorithms.md#roguelike.algorithms.mob_algorithm.MobAlgorithm)
  * [roguelike.algorithms.simple_algo module](roguelike.algorithms.md#module-roguelike.algorithms.simple_algo)
    * [`SimpleAlgo`](roguelike.algorithms.md#roguelike.algorithms.simple_algo.SimpleAlgo)
      * [`SimpleAlgo.move()`](roguelike.algorithms.md#roguelike.algorithms.simple_algo.SimpleAlgo.move)
      * [`SimpleAlgo.shift_down()`](roguelike.algorithms.md#roguelike.algorithms.simple_algo.SimpleAlgo.shift_down)
      * [`SimpleAlgo.shift_left()`](roguelike.algorithms.md#roguelike.algorithms.simple_algo.SimpleAlgo.shift_left)
      * [`SimpleAlgo.shift_right()`](roguelike.algorithms.md#roguelike.algorithms.simple_algo.SimpleAlgo.shift_right)
      * [`SimpleAlgo.shift_up()`](roguelike.algorithms.md#roguelike.algorithms.simple_algo.SimpleAlgo.shift_up)
  * [Module contents](roguelike.algorithms.md#module-roguelike.algorithms)
* [roguelike.common package](roguelike.common.md)
  * [Submodules](roguelike.common.md#submodules)
  * [roguelike.common.common module](roguelike.common.md#module-roguelike.common.common)
    * [`Coordinate`](roguelike.common.md#roguelike.common.common.Coordinate)
  * [Module contents](roguelike.common.md#module-roguelike.common)
* [roguelike.entities package](roguelike.entities.md)
  * [Submodules](roguelike.entities.md#submodules)
  * [roguelike.entities.abstract_object module](roguelike.entities.md#module-roguelike.entities.abstract_object)
    * [`AbstractObject`](roguelike.entities.md#roguelike.entities.abstract_object.AbstractObject)
      * [`AbstractObject.get_label()`](roguelike.entities.md#roguelike.entities.abstract_object.AbstractObject.get_label)
      * [`AbstractObject.get_resources_path()`](roguelike.entities.md#roguelike.entities.abstract_object.AbstractObject.get_resources_path)
  * [roguelike.entities.artifact module](roguelike.entities.md#module-roguelike.entities.artifact)
    * [`Artifact`](roguelike.entities.md#roguelike.entities.artifact.Artifact)
      * [`Artifact.get_label()`](roguelike.entities.md#roguelike.entities.artifact.Artifact.get_label)
    * [`Shield`](roguelike.entities.md#roguelike.entities.artifact.Shield)
      * [`Shield.get_label()`](roguelike.entities.md#roguelike.entities.artifact.Shield.get_label)
    * [`Weapon`](roguelike.entities.md#roguelike.entities.artifact.Weapon)
      * [`Weapon.get_label()`](roguelike.entities.md#roguelike.entities.artifact.Weapon.get_label)
  * [roguelike.entities.mob module](roguelike.entities.md#module-roguelike.entities.mob)
    * [`Mob`](roguelike.entities.md#roguelike.entities.mob.Mob)
      * [`Mob.get_label()`](roguelike.entities.md#roguelike.entities.mob.Mob.get_label)
      * [`Mob.move()`](roguelike.entities.md#roguelike.entities.mob.Mob.move)
  * [roguelike.entities.user module](roguelike.entities.md#module-roguelike.entities.user)
    * [`User`](roguelike.entities.md#roguelike.entities.user.User)
      * [`User.get_item()`](roguelike.entities.md#roguelike.entities.user.User.get_item)
      * [`User.get_label()`](roguelike.entities.md#roguelike.entities.user.User.get_label)
      * [`User.shift_down()`](roguelike.entities.md#roguelike.entities.user.User.shift_down)
      * [`User.shift_left()`](roguelike.entities.md#roguelike.entities.user.User.shift_left)
      * [`User.shift_right()`](roguelike.entities.md#roguelike.entities.user.User.shift_right)
      * [`User.shift_up()`](roguelike.entities.md#roguelike.entities.user.User.shift_up)
      * [`User.throw_item()`](roguelike.entities.md#roguelike.entities.user.User.throw_item)
  * [roguelike.entities.wall module](roguelike.entities.md#module-roguelike.entities.wall)
    * [`Wall`](roguelike.entities.md#roguelike.entities.wall.Wall)
      * [`Wall.get_label()`](roguelike.entities.md#roguelike.entities.wall.Wall.get_label)
  * [Module contents](roguelike.entities.md#module-roguelike.entities)
* [roguelike.map package](roguelike.map.md)
  * [Submodules](roguelike.map.md#submodules)
  * [roguelike.map.map module](roguelike.map.md#module-roguelike.map.map)
    * [`GameMap`](roguelike.map.md#roguelike.map.map.GameMap)
      * [`GameMap.check_walls()`](roguelike.map.md#roguelike.map.map.GameMap.check_walls)
  * [roguelike.map.map_generator module](roguelike.map.md#module-roguelike.map.map_generator)
    * [`MapGenerator`](roguelike.map.md#roguelike.map.map_generator.MapGenerator)
      * [`MapGenerator.create_map()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.create_map)
      * [`MapGenerator.generate_random_enemies()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_enemies)
      * [`MapGenerator.generate_random_items()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_items)
      * [`MapGenerator.generate_random_user()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_user)
      * [`MapGenerator.generate_random_walls()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_walls)
    * [`MapGeneratorException`](roguelike.map.md#roguelike.map.map_generator.MapGeneratorException)
  * [Module contents](roguelike.map.md#module-roguelike.map)

## Submodules

## roguelike.game module

### *class* roguelike.game.Game

Базовые классы: `object`

Game logic.

#### get_item() → None

get_item logic.

#### get_walls() → list[tuple[int, int]]

get_walls logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  list[tuple[int, int]]

#### run() → None

Run logic.

* **Тип результата:**
  None

#### shift_down() → None

shift_down logic.

#### shift_left() → None

shift_left logic.

#### shift_right() → None

shift_right logic.

#### shift_up() → None

shift_up logic.

#### throw_item() → None

throw_item logic.

* **Тип результата:**
  None

## roguelike.main module

### roguelike.main.main() → None

Main logic.

## Module contents
