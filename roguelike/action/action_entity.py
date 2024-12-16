from abc import abstractmethod

from roguelike.entities.abstract_object import AbstractObject


SHIFT_UP = 0
SHIFT_DOWN = 1
SHIFT_LEFT = 2
SHIFT_RIGHT = 3
DEACTIVATE_ITEM = 4
ACTIVATE_ITEM = 5
GET_ITEM = 6

class Action:
    @abstractmethod
    def __init__(self, type: int) -> None:
        self.type = type

class MovingAction(Action):
    def __init__(self, type: int, entity : AbstractObject) -> None:
        super().__init__(type)
        self.entity = entity


class ItemAction(Action):
    def __init__(self, type: int, id : int) -> None:
        super().__init__(type)
        self.id = id

