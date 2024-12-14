from typing import List

from roguelike.entities import artifact
from roguelike.entities.artifact import Artifact
from roguelike.entities.inventory_slot import InventorySlot
from roguelike.inventory.stats_change import StatsChange


class Inventory():
    """Inventory logic."""

    def __init__(
        self,
        inventory: List[InventorySlot],
        active_items: List[InventorySlot],
    ):
        self.inventory = inventory
        self.active_items = active_items

    def add_item(self, item: Artifact)-> StatsChange:
        stats = StatsChange(damage=0, health=0)

        for active_item in self.active_items:
            if active_item.item == None:
                active_item.item = item
                item.teleport(active_item.xcor(), active_item.ycor())
                self.activate_stats(active_item.item, stats, 1)

                return stats

        for slot in self.inventory:
            if slot.item == None:
                slot.item = item
                item.teleport(slot.xcor(), slot.ycor())
                return stats

        return stats

    def activate_stats(self, item: Artifact, stats: StatsChange, coef: int):
        if isinstance(item, artifact.Weapon):
            stats.damage += coef * item.bonus_value
        elif isinstance(item, artifact.Shield):
            stats.health += coef * item.bonus_value


    def move_item(self, slot: InventorySlot, item: Artifact):
        slot.item = item
        item.teleport(slot.xcor(), slot.ycor())


    def activate_item(self, index: int)-> StatsChange:
        stats = StatsChange(damage=0, health=0)

        item_to_activate = self.inventory[index].item
        if item_to_activate == None:
            return stats

        self.activate_stats(item_to_activate, stats, 1)

        self.inventory[index].item = None

        for active_item in self.active_items:
            if active_item.item == None:
                active_item.item = item_to_activate
                item_to_activate.teleport(active_item.xcor(), active_item.ycor())
                return stats

        item_to_deactivate = self.active_items[0].item

        self.move_item(slot=self.active_items[0], item=item_to_activate)

        self.move_item(slot=self.inventory[index], item=item_to_deactivate)
        self.activate_stats(item_to_deactivate, stats, -1)

        return stats


    def deactivate_item(self, index: int) -> StatsChange:
        stats = StatsChange(damage=0, health=0)

        deactivate_item = self.active_items[index].item

        self.activate_stats(deactivate_item, stats, -1)

        if deactivate_item == None:
            return stats

        self.active_items[index].item = None

        for slot in self.inventory:
            if slot.item == None:
                slot.item = deactivate_item
                deactivate_item.teleport(slot.xcor(), slot.ycor())

                return stats

        inventory_item = self.inventory[0].item

        self.move_item(slot=self.inventory[0], item=deactivate_item)

        self.move_item(slot=self.active_items[index], item=inventory_item)

        self.activate_stats(inventory_item, stats, 1)


        return stats