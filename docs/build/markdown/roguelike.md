# roguelike package

## Subpackages

* [roguelike.action package](roguelike.action.md)
  * [Submodules](roguelike.action.md#submodules)
  * [roguelike.action.action_entity module](roguelike.action.md#module-roguelike.action.action_entity)
    * [`Action`](roguelike.action.md#roguelike.action.action_entity.Action)
      * [`Action.run()`](roguelike.action.md#roguelike.action.action_entity.Action.run)
    * [`ItemAction`](roguelike.action.md#roguelike.action.action_entity.ItemAction)
      * [`ItemAction.run()`](roguelike.action.md#roguelike.action.action_entity.ItemAction.run)
    * [`MovingAction`](roguelike.action.md#roguelike.action.action_entity.MovingAction)
      * [`MovingAction.run()`](roguelike.action.md#roguelike.action.action_entity.MovingAction.run)
    * [`SpellAction`](roguelike.action.md#roguelike.action.action_entity.SpellAction)
      * [`SpellAction.run()`](roguelike.action.md#roguelike.action.action_entity.SpellAction.run)
  * [Module contents](roguelike.action.md#module-roguelike.action)
* [roguelike.algorithms package](roguelike.algorithms.md)
  * [Submodules](roguelike.algorithms.md#submodules)
  * [roguelike.algorithms.agressive_algo module](roguelike.algorithms.md#module-roguelike.algorithms.agressive_algo)
    * [`AgressiveAlgo`](roguelike.algorithms.md#roguelike.algorithms.agressive_algo.AgressiveAlgo)
      * [`AgressiveAlgo.move()`](roguelike.algorithms.md#roguelike.algorithms.agressive_algo.AgressiveAlgo.move)
  * [roguelike.algorithms.coward_algo module](roguelike.algorithms.md#module-roguelike.algorithms.coward_algo)
    * [`CowardAlgo`](roguelike.algorithms.md#roguelike.algorithms.coward_algo.CowardAlgo)
      * [`CowardAlgo.move()`](roguelike.algorithms.md#roguelike.algorithms.coward_algo.CowardAlgo.move)
  * [roguelike.algorithms.mob_algorithm module](roguelike.algorithms.md#module-roguelike.algorithms.mob_algorithm)
    * [`MobAlgorithm`](roguelike.algorithms.md#roguelike.algorithms.mob_algorithm.MobAlgorithm)
      * [`MobAlgorithm.move()`](roguelike.algorithms.md#roguelike.algorithms.mob_algorithm.MobAlgorithm.move)
  * [roguelike.algorithms.mob_decorator module](roguelike.algorithms.md#module-roguelike.algorithms.mob_decorator)
    * [`AbstractDecorator`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator.AbstractDecorator)
      * [`AbstractDecorator.move()`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator.AbstractDecorator.move)
  * [roguelike.algorithms.mob_decorator_confused module](roguelike.algorithms.md#module-roguelike.algorithms.mob_decorator_confused)
    * [`ConfusedDecorator`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator_confused.ConfusedDecorator)
      * [`ConfusedDecorator.move()`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator_confused.ConfusedDecorator.move)
      * [`ConfusedDecorator.shift_down()`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator_confused.ConfusedDecorator.shift_down)
      * [`ConfusedDecorator.shift_left()`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator_confused.ConfusedDecorator.shift_left)
      * [`ConfusedDecorator.shift_right()`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator_confused.ConfusedDecorator.shift_right)
      * [`ConfusedDecorator.shift_up()`](roguelike.algorithms.md#roguelike.algorithms.mob_decorator_confused.ConfusedDecorator.shift_up)
  * [roguelike.algorithms.passive_algo module](roguelike.algorithms.md#module-roguelike.algorithms.passive_algo)
    * [`PassiveAlgo`](roguelike.algorithms.md#roguelike.algorithms.passive_algo.PassiveAlgo)
      * [`PassiveAlgo.move()`](roguelike.algorithms.md#roguelike.algorithms.passive_algo.PassiveAlgo.move)
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
  * [roguelike.entities.copy_mob module](roguelike.entities.md#module-roguelike.entities.copy_mob)
    * [`CopyMob`](roguelike.entities.md#roguelike.entities.copy_mob.CopyMob)
      * [`CopyMob.clone()`](roguelike.entities.md#roguelike.entities.copy_mob.CopyMob.clone)
  * [roguelike.entities.dragon module](roguelike.entities.md#module-roguelike.entities.dragon)
    * [`Dragon`](roguelike.entities.md#roguelike.entities.dragon.Dragon)
  * [roguelike.entities.image module](roguelike.entities.md#module-roguelike.entities.image)
    * [`Image`](roguelike.entities.md#roguelike.entities.image.Image)
      * [`Image.get_label()`](roguelike.entities.md#roguelike.entities.image.Image.get_label)
  * [roguelike.entities.inventory_slot module](roguelike.entities.md#module-roguelike.entities.inventory_slot)
    * [`InventorySlot`](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot)
      * [`InventorySlot.get_label()`](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot.get_label)
  * [roguelike.entities.mob module](roguelike.entities.md#module-roguelike.entities.mob)
    * [`Mob`](roguelike.entities.md#roguelike.entities.mob.Mob)
      * [`Mob.get_label()`](roguelike.entities.md#roguelike.entities.mob.Mob.get_label)
      * [`Mob.move()`](roguelike.entities.md#roguelike.entities.mob.Mob.move)
  * [roguelike.entities.simple_mob module](roguelike.entities.md#module-roguelike.entities.simple_mob)
    * [`SimpleMob`](roguelike.entities.md#roguelike.entities.simple_mob.SimpleMob)
  * [roguelike.entities.skeleton module](roguelike.entities.md#module-roguelike.entities.skeleton)
    * [`Skeleton`](roguelike.entities.md#roguelike.entities.skeleton.Skeleton)
  * [roguelike.entities.text_object module](roguelike.entities.md#module-roguelike.entities.text_object)
    * [`TextObject`](roguelike.entities.md#roguelike.entities.text_object.TextObject)
      * [`TextObject.get_label()`](roguelike.entities.md#roguelike.entities.text_object.TextObject.get_label)
  * [roguelike.entities.user module](roguelike.entities.md#module-roguelike.entities.user)
    * [`User`](roguelike.entities.md#roguelike.entities.user.User)
      * [`User.get_label()`](roguelike.entities.md#roguelike.entities.user.User.get_label)
  * [roguelike.entities.wall module](roguelike.entities.md#module-roguelike.entities.wall)
    * [`Wall`](roguelike.entities.md#roguelike.entities.wall.Wall)
      * [`Wall.get_label()`](roguelike.entities.md#roguelike.entities.wall.Wall.get_label)
  * [Module contents](roguelike.entities.md#module-roguelike.entities)
* [roguelike.inventory package](roguelike.inventory.md)
  * [Submodules](roguelike.inventory.md#submodules)
  * [roguelike.inventory.inventory module](roguelike.inventory.md#module-roguelike.inventory.inventory)
    * [`Inventory`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory)
      * [`Inventory.inventory`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory.inventory)
      * [`Inventory.active_items`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory.active_items)
      * [`Inventory.activate_item()`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory.activate_item)
      * [`Inventory.activate_stats()`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory.activate_stats)
      * [`Inventory.add_item()`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory.add_item)
      * [`Inventory.deactivate_item()`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory.deactivate_item)
      * [`Inventory.move_item()`](roguelike.inventory.md#roguelike.inventory.inventory.Inventory.move_item)
  * [roguelike.inventory.stats_change module](roguelike.inventory.md#module-roguelike.inventory.stats_change)
    * [`StatsChange`](roguelike.inventory.md#roguelike.inventory.stats_change.StatsChange)
      * [`StatsChange.damage`](roguelike.inventory.md#roguelike.inventory.stats_change.StatsChange.damage)
      * [`StatsChange.health`](roguelike.inventory.md#roguelike.inventory.stats_change.StatsChange.health)
  * [Module contents](roguelike.inventory.md#module-roguelike.inventory)
* [roguelike.map package](roguelike.map.md)
  * [Submodules](roguelike.map.md#submodules)
  * [roguelike.map.map module](roguelike.map.md#module-roguelike.map.map)
    * [`GameMap`](roguelike.map.md#roguelike.map.map.GameMap)
      * [`GameMap.check_walls()`](roguelike.map.md#roguelike.map.map.GameMap.check_walls)
      * [`GameMap.is_user()`](roguelike.map.md#roguelike.map.map.GameMap.is_user)
  * [roguelike.map.map_generator module](roguelike.map.md#module-roguelike.map.map_generator)
    * [`MapGenerator`](roguelike.map.md#roguelike.map.map_generator.MapGenerator)
      * [`MapGenerator.create_map()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.create_map)
      * [`MapGenerator.generate_inventory()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_inventory)
      * [`MapGenerator.generate_random_enemies()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_enemies)
      * [`MapGenerator.generate_random_items()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_items)
      * [`MapGenerator.generate_random_user()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_user)
      * [`MapGenerator.generate_random_walls()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_random_walls)
      * [`MapGenerator.generate_stats()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.generate_stats)
      * [`MapGenerator.get_mob()`](roguelike.map.md#roguelike.map.map_generator.MapGenerator.get_mob)
    * [`MapGeneratorException`](roguelike.map.md#roguelike.map.map_generator.MapGeneratorException)
  * [Module contents](roguelike.map.md#module-roguelike.map)
* [roguelike.mob_factory package](roguelike.mob_factory.md)
  * [Submodules](roguelike.mob_factory.md#submodules)
  * [roguelike.mob_factory.agressive_mobs_factory module](roguelike.mob_factory.md#module-roguelike.mob_factory.agressive_mobs_factory)
    * [`AggressiveMobsFactory`](roguelike.mob_factory.md#roguelike.mob_factory.agressive_mobs_factory.AggressiveMobsFactory)
      * [`AggressiveMobsFactory.create_copy_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.agressive_mobs_factory.AggressiveMobsFactory.create_copy_mob)
      * [`AggressiveMobsFactory.create_dragon()`](roguelike.mob_factory.md#roguelike.mob_factory.agressive_mobs_factory.AggressiveMobsFactory.create_dragon)
      * [`AggressiveMobsFactory.create_simple_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.agressive_mobs_factory.AggressiveMobsFactory.create_simple_mob)
      * [`AggressiveMobsFactory.create_skeleton()`](roguelike.mob_factory.md#roguelike.mob_factory.agressive_mobs_factory.AggressiveMobsFactory.create_skeleton)
  * [roguelike.mob_factory.cowards_mobs_factory module](roguelike.mob_factory.md#module-roguelike.mob_factory.cowards_mobs_factory)
    * [`CowardMobsFactory`](roguelike.mob_factory.md#roguelike.mob_factory.cowards_mobs_factory.CowardMobsFactory)
      * [`CowardMobsFactory.create_copy_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.cowards_mobs_factory.CowardMobsFactory.create_copy_mob)
      * [`CowardMobsFactory.create_dragon()`](roguelike.mob_factory.md#roguelike.mob_factory.cowards_mobs_factory.CowardMobsFactory.create_dragon)
      * [`CowardMobsFactory.create_simple_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.cowards_mobs_factory.CowardMobsFactory.create_simple_mob)
      * [`CowardMobsFactory.create_skeleton()`](roguelike.mob_factory.md#roguelike.mob_factory.cowards_mobs_factory.CowardMobsFactory.create_skeleton)
  * [roguelike.mob_factory.mob_factory module](roguelike.mob_factory.md#module-roguelike.mob_factory.mob_factory)
    * [`MobFactory`](roguelike.mob_factory.md#roguelike.mob_factory.mob_factory.MobFactory)
      * [`MobFactory.create_copy_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.mob_factory.MobFactory.create_copy_mob)
      * [`MobFactory.create_dragon()`](roguelike.mob_factory.md#roguelike.mob_factory.mob_factory.MobFactory.create_dragon)
      * [`MobFactory.create_random_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.mob_factory.MobFactory.create_random_mob)
      * [`MobFactory.create_simple_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.mob_factory.MobFactory.create_simple_mob)
      * [`MobFactory.create_skeleton()`](roguelike.mob_factory.md#roguelike.mob_factory.mob_factory.MobFactory.create_skeleton)
  * [roguelike.mob_factory.passive_mobs_factory module](roguelike.mob_factory.md#module-roguelike.mob_factory.passive_mobs_factory)
    * [`PassiveMobsFactory`](roguelike.mob_factory.md#roguelike.mob_factory.passive_mobs_factory.PassiveMobsFactory)
      * [`PassiveMobsFactory.create_copy_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.passive_mobs_factory.PassiveMobsFactory.create_copy_mob)
      * [`PassiveMobsFactory.create_dragon()`](roguelike.mob_factory.md#roguelike.mob_factory.passive_mobs_factory.PassiveMobsFactory.create_dragon)
      * [`PassiveMobsFactory.create_simple_mob()`](roguelike.mob_factory.md#roguelike.mob_factory.passive_mobs_factory.PassiveMobsFactory.create_simple_mob)
      * [`PassiveMobsFactory.create_skeleton()`](roguelike.mob_factory.md#roguelike.mob_factory.passive_mobs_factory.PassiveMobsFactory.create_skeleton)
  * [Module contents](roguelike.mob_factory.md#module-roguelike.mob_factory)
* [roguelike.state package](roguelike.state.md)
  * [Submodules](roguelike.state.md#submodules)
  * [roguelike.state.bravery_state module](roguelike.state.md#module-roguelike.state.bravery_state)
    * [`BraveryState`](roguelike.state.md#roguelike.state.bravery_state.BraveryState)
      * [`BraveryState.move()`](roguelike.state.md#roguelike.state.bravery_state.BraveryState.move)
  * [roguelike.state.default_state module](roguelike.state.md#module-roguelike.state.default_state)
    * [`DefaultState`](roguelike.state.md#roguelike.state.default_state.DefaultState)
      * [`DefaultState.move()`](roguelike.state.md#roguelike.state.default_state.DefaultState.move)
    * [`check_is_someone_near()`](roguelike.state.md#roguelike.state.default_state.check_is_someone_near)
  * [roguelike.state.mob_state module](roguelike.state.md#module-roguelike.state.mob_state)
    * [`MobState`](roguelike.state.md#roguelike.state.mob_state.MobState)
      * [`MobState.move()`](roguelike.state.md#roguelike.state.mob_state.MobState.move)
  * [roguelike.state.panic_state module](roguelike.state.md#module-roguelike.state.panic_state)
    * [`PanicState`](roguelike.state.md#roguelike.state.panic_state.PanicState)
      * [`PanicState.move()`](roguelike.state.md#roguelike.state.panic_state.PanicState.move)
  * [Module contents](roguelike.state.md#module-roguelike.state)

## Submodules

## roguelike.game module

### *class* roguelike.game.Game

Базовые классы: `object`

Game logic.

#### activate_item(i: int) → Callable[[], None]

activate_item logic.

#### battle_with_mob(mob: [Mob](roguelike.entities.md#roguelike.entities.mob.Mob)) → None

Function with battle logic.

#### clone(mob: [CopyMob](roguelike.entities.md#roguelike.entities.copy_mob.CopyMob)) → Any

Clone logic.

* **Параметры:**
  **mob** ([*CopyMob*](roguelike.entities.md#roguelike.entities.copy_mob.CopyMob)) – Description of mob.
* **Результат:**
  Description of return value
* **Тип результата:**
  *Any*

#### confused() → None

deactivate_item logic.

#### deactivate_item(i: int) → Callable[[], None]

deactivate_item logic.

#### get_item() → None

get_item logic.

#### get_walls() → list[tuple[int, int]]

Walls getter.

* **Результат:**
  Description of return value
* **Тип результата:**
  list[tuple[int, int]]

#### process_queue(has_resist: int) → int

Command queue processing.

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

## roguelike.main module

### roguelike.main.main() → None

Main logic.

## roguelike.user_controller module

### *class* roguelike.user_controller.UserController(user: [User](roguelike.entities.md#roguelike.entities.user.User), game_map: Any, move_size: int)

Базовые классы: `object`

UserController logic.

#### activate_item(index: int) → None

throw_item logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### deactivate_item(index: int) → None

throw_item logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### get_item() → None

get_item logic.

* **Параметры:**
  **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_down() → None

shift_down logic.

* **Параметры:**
  **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_left() → None

shift_left logic.

* **Параметры:**
  **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_right() → None

shift_right logic.

* **Параметры:**
  **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### shift_up() → None

shift_up logic.

* **Параметры:**
  **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.
* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### update_damage(delta: int) → None

update_damage logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### update_health(delta: int) → None

update_health logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### update_level() → None

update_health logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

#### update_xp(delta: int) → None

update_health logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  None

## Module contents
