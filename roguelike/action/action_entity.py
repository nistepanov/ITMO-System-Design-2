from abc import abstractmethod

from roguelike.algorithms.mob_decorator_confused import ConfusedDecorator
from roguelike.entities.abstract_object import AbstractObject
from roguelike.entities.user import User
from roguelike.map.map import GameMap
from roguelike.user_controller import UserController


SHIFT_UP = 0
SHIFT_DOWN = 1
SHIFT_LEFT = 2
SHIFT_RIGHT = 3
DEACTIVATE_ITEM = 4
ACTIVATE_ITEM = 5
GET_ITEM = 6
CONFUSED = 7


class Action:
    """Action logic."""

    @abstractmethod
    def __init__(self, type: int) -> None:
        self.type = type

    @abstractmethod
    def run(self):
        raise NotImplementedError


class MovingAction(Action):
    """MovingAction logic."""

    def __init__(self, type: int, entity: AbstractObject, user_controller: UserController) -> None:
        super().__init__(type)
        self.entity = entity
        self.user_controller = user_controller
    
    def run(self):
        if self.type == SHIFT_UP:
            self.user_controller.shift_up()
        if self.type == SHIFT_DOWN:
            self.user_controller.shift_down()
        if self.type == SHIFT_LEFT:
            self.user_controller.shift_left()
        if self.type == SHIFT_RIGHT:
            self.user_controller.shift_right()


class ItemAction(Action):
    """ItemAction logic."""

    def __init__(self, type: int, id: int, user_controller: UserController) -> None:
        super().__init__(type)
        self.id = id
        self.user_controller = user_controller

    def run(self):
        if self.type == DEACTIVATE_ITEM:
            self.user_controller.deactivate_item(self.id)
        elif self.type == ACTIVATE_ITEM:
            self.user_controller.activate_item(self.id)
        elif self.type == GET_ITEM:
            self.user_controller.get_item()


class SpellAction(Action):
    """ItemAction logic."""

    def __init__(self, type: int, map: GameMap, user: User) -> None:
        super().__init__(type)
        self.map = map
        self.user = user

    def run(self):
        if self.type == CONFUSED:
            x = self.user.xcor()
            y = self.user.ycor()
            shifts = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]
            for mob in self.map.mobs:
                for shift in shifts:
                    if mob.xcor() == x + shift[0] * self.move_size and mob.ycor() == y + shift[1] * self.move_size:
                        mob.algo = ConfusedDecorator(10, mob.algo)
