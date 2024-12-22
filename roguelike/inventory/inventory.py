from roguelike.entities import artifact
from roguelike.entities.artifact import Artifact
from roguelike.entities.inventory_slot import InventorySlot
from roguelike.inventory.stats_change import StatsChange


class Inventory:
    """Represents the inventory logic, including adding, moving, activating, and deactivating items.

    Attributes:
        inventory (list[InventorySlot]): The list of inventory slots.
        active_items (list[InventorySlot]): The list of active item slots.
    """

    def __init__(
        self,
        inventory: list[InventorySlot],
        active_items: list[InventorySlot],
    ) -> None:
        """Initialize an Inventory instance.

        Args:
            inventory (list[InventorySlot]): The inventory slots.
            active_items (list[InventorySlot]): The active item slots.
        """
        self.inventory = inventory
        self.active_items = active_items

    def add_item(self, item: Artifact) -> StatsChange:
        """Add an item to the inventory or activate it if possible.

        Args:
            item (Artifact): The item to add.

        Returns:
            StatsChange: The resulting stats change from adding the item.
        """
        stats = StatsChange(damage=0, health=0)

        # Try to place the item in an active slot first.
        for active_item in self.active_items:
            if active_item.item is None:
                active_item.item = item
                item.teleport(active_item.xcor(), active_item.ycor())
                self.activate_stats(active_item.item, stats, 1)
                return stats

        # If no active slot is available, place the item in the inventory.
        for slot in self.inventory:
            if slot.item is None:
                slot.item = item
                item.teleport(slot.xcor(), slot.ycor())
                return stats

        return stats  # No slots available.

    def activate_stats(self, item: Artifact, stats: StatsChange, coef: int) -> None:
        """Modify stats based on the item's type and coefficient.

        Args:
            item (Artifact): The item affecting stats.
            stats (StatsChange): The stats to modify.
            coef (int): The coefficient (1 for activation, -1 for deactivation).
        """
        if isinstance(item, artifact.Weapon):
            stats.damage += coef * item.bonus_value
        elif isinstance(item, artifact.Shield):
            stats.health += coef * item.bonus_value

    def move_item(self, slot: InventorySlot, item: Artifact) -> None:
        """Move an item to a specific slot.

        Args:
            slot (InventorySlot): The destination slot.
            item (Artifact): The item to move.
        """
        slot.item = item
        item.teleport(slot.xcor(), slot.ycor())

    def activate_item(self, index: int) -> StatsChange:
        """Activate an item from the inventory.

        Args:
            index (int): The index of the inventory slot containing the item.

        Returns:
            StatsChange: The resulting stats change from activation.
        """
        stats = StatsChange(damage=0, health=0)

        item_to_activate = self.inventory[index].item
        if item_to_activate is None:
            return stats

        # Activate stats for the selected item.
        self.activate_stats(item_to_activate, stats, 1)
        self.inventory[index].item = None

        # Place the item in the first available active slot.
        for active_item in self.active_items:
            if active_item.item is None:
                active_item.item = item_to_activate
                item_to_activate.teleport(active_item.xcor(), active_item.ycor())
                return stats

        self.move_item(slot=self.active_items[0], item=item_to_activate)

        # If no active slot is available, swap with the first active item.
        item_to_deactivate = self.active_items[0].item
        if item_to_deactivate is None:
            return stats

        self.move_item(slot=self.inventory[index], item=item_to_deactivate)
        self.activate_stats(item_to_deactivate, stats, -1)

        return stats

    def deactivate_item(self, index: int) -> StatsChange:
        """Deactivate an active item.

        Args:
            index (int): The index of the active slot containing the item.

        Returns:
            StatsChange: The resulting stats change from deactivation.
        """
        stats = StatsChange(damage=0, health=0)

        deactivate_item = self.active_items[index].item
        if deactivate_item is None:
            return stats

        # Deactivate stats for the selected item.
        self.activate_stats(deactivate_item, stats, -1)
        self.active_items[index].item = None

        # Place the item in the first available inventory slot.
        for slot in self.inventory:
            if slot.item is None:
                slot.item = deactivate_item
                deactivate_item.teleport(slot.xcor(), slot.ycor())
                return stats

        self.move_item(slot=self.inventory[0], item=deactivate_item)

        # If no inventory slot is available, swap with the first inventory item.
        inventory_item = self.inventory[0].item
        if inventory_item is None:
            return stats

        self.move_item(slot=self.active_items[index], item=inventory_item)
        self.activate_stats(inventory_item, stats, 1)

        return stats
