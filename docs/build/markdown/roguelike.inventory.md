# roguelike.inventory package

## Submodules

## roguelike.inventory.inventory module

### *class* roguelike.inventory.inventory.Inventory(inventory: list[[InventorySlot](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot)], active_items: list[[InventorySlot](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot)])

Базовые классы: `object`

Represents the inventory logic, including adding, moving, activating, and deactivating items.

#### inventory

The list of inventory slots.

* **Type:**
  list[[InventorySlot](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot)]

#### active_items

The list of active item slots.

* **Type:**
  list[[InventorySlot](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot)]

#### activate_item(index: int) → [StatsChange](#roguelike.inventory.stats_change.StatsChange)

Activate an item from the inventory.

* **Параметры:**
  **index** (*int*) – The index of the inventory slot containing the item.
* **Результат:**
  The resulting stats change from activation.
* **Тип результата:**
  [StatsChange](#roguelike.inventory.stats_change.StatsChange)

#### activate_stats(item: [Artifact](roguelike.entities.md#roguelike.entities.artifact.Artifact), stats: [StatsChange](#roguelike.inventory.stats_change.StatsChange), coef: int) → None

Modify stats based on the item’s type and coefficient.

* **Параметры:**
  * **item** ([*Artifact*](roguelike.entities.md#roguelike.entities.artifact.Artifact)) – The item affecting stats.
  * **stats** ([*StatsChange*](#roguelike.inventory.stats_change.StatsChange)) – The stats to modify.
  * **coef** (*int*) – The coefficient (1 for activation, -1 for deactivation).

#### add_item(item: [Artifact](roguelike.entities.md#roguelike.entities.artifact.Artifact)) → [StatsChange](#roguelike.inventory.stats_change.StatsChange)

Add an item to the inventory or activate it if possible.

* **Параметры:**
  **item** ([*Artifact*](roguelike.entities.md#roguelike.entities.artifact.Artifact)) – The item to add.
* **Результат:**
  The resulting stats change from adding the item.
* **Тип результата:**
  [StatsChange](#roguelike.inventory.stats_change.StatsChange)

#### deactivate_item(index: int) → [StatsChange](#roguelike.inventory.stats_change.StatsChange)

Deactivate an active item.

* **Параметры:**
  **index** (*int*) – The index of the active slot containing the item.
* **Результат:**
  The resulting stats change from deactivation.
* **Тип результата:**
  [StatsChange](#roguelike.inventory.stats_change.StatsChange)

#### move_item(slot: [InventorySlot](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot), item: [Artifact](roguelike.entities.md#roguelike.entities.artifact.Artifact)) → None

Move an item to a specific slot.

* **Параметры:**
  * **slot** ([*InventorySlot*](roguelike.entities.md#roguelike.entities.inventory_slot.InventorySlot)) – The destination slot.
  * **item** ([*Artifact*](roguelike.entities.md#roguelike.entities.artifact.Artifact)) – The item to move.

## roguelike.inventory.stats_change module

### *class* roguelike.inventory.stats_change.StatsChange(damage: int, health: int)

Базовые классы: `object`

A class representing changes to an entity’s stats.

#### damage

The change in damage value.

* **Type:**
  int

#### health

The change in health value.

* **Type:**
  int

## Module contents
