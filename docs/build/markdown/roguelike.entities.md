# roguelike.entities package

## Submodules

## roguelike.entities.abstract_object module

### *class* roguelike.entities.abstract_object.AbstractObject

Базовые классы: `Turtle`

AbstractObject logic.

#### *abstract static* get_label() → str

get_label logic.

#### *static* get_resources_path() → str

get_resources_path logic.

## roguelike.entities.artifact module

### *class* roguelike.entities.artifact.Artifact(bonus_value: int)

Базовые классы: [`AbstractObject`](#roguelike.entities.abstract_object.AbstractObject)

Artifact logic.

#### *static* get_label() → str

get_label logic.

### *class* roguelike.entities.artifact.Shield(bonus_value: int)

Базовые классы: [`Artifact`](#roguelike.entities.artifact.Artifact)

Shield logic.

#### *static* get_label() → str

get_label logic.

### *class* roguelike.entities.artifact.Weapon(bonus_value: int)

Базовые классы: [`Artifact`](#roguelike.entities.artifact.Artifact)

Weapon logic.

#### *static* get_label() → str

get_label logic.

## roguelike.entities.copy_mob module

### *class* roguelike.entities.copy_mob.CopyMob(algo: Any)

Базовые классы: [`Mob`](#roguelike.entities.mob.Mob)

CopyMob mob class.

#### clone() → Any

Clone logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  [Mob](#roguelike.entities.mob.Mob)

## roguelike.entities.dragon module

### *class* roguelike.entities.dragon.Dragon(algo: Any)

Базовые классы: [`Mob`](#roguelike.entities.mob.Mob)

Dragon mob class.

## roguelike.entities.image module

### *class* roguelike.entities.image.Image(image_path: str)

Базовые классы: [`AbstractObject`](#roguelike.entities.abstract_object.AbstractObject)

Image logic.

#### *static* get_label() → str

get_label logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  str

## roguelike.entities.inventory_slot module

### *class* roguelike.entities.inventory_slot.InventorySlot

Базовые классы: [`AbstractObject`](#roguelike.entities.abstract_object.AbstractObject)

InventorySlot logic.

#### *static* get_label() → str

get_label logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  str

## roguelike.entities.mob module

### *class* roguelike.entities.mob.Mob(algo: Any)

Базовые классы: [`AbstractObject`](#roguelike.entities.abstract_object.AbstractObject)

Mob logic.

#### *static* get_label() → str

get_label logic.

#### move(game_map: Any) → tuple[float, float] | None

Move logic.

* **Параметры:**
  **game_map** ([*GameMap*](roguelike.map.md#roguelike.map.map.GameMap)) – Description of game_map.

## roguelike.entities.simple_mob module

### *class* roguelike.entities.simple_mob.SimpleMob(algo: Any)

Базовые классы: [`Mob`](#roguelike.entities.mob.Mob)

Dragon mob class.

## roguelike.entities.skeleton module

### *class* roguelike.entities.skeleton.Skeleton(algo: Any)

Базовые классы: [`Mob`](#roguelike.entities.mob.Mob)

Skeleton mob class.

## roguelike.entities.text_object module

### *class* roguelike.entities.text_object.TextObject

Базовые классы: [`AbstractObject`](#roguelike.entities.abstract_object.AbstractObject)

Text logic.

#### *static* get_label() → str

get_label logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  str

## roguelike.entities.user module

### *class* roguelike.entities.user.User(health: int, damage: int, level: int, inventory: [Inventory](roguelike.inventory.md#roguelike.inventory.inventory.Inventory))

Базовые классы: [`AbstractObject`](#roguelike.entities.abstract_object.AbstractObject)

User logic.

#### *static* get_label() → str

get_label logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  str

## roguelike.entities.wall module

### *class* roguelike.entities.wall.Wall

Базовые классы: [`AbstractObject`](#roguelike.entities.abstract_object.AbstractObject)

Wall logic.

#### *static* get_label() → str

get_label logic.

* **Результат:**
  Description of return value
* **Тип результата:**
  str

## Module contents
