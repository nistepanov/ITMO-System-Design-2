from unittest.mock import MagicMock

import pytest

from roguelike.action.action_entity import (
    CONFUSED,
    SHIFT_DOWN,
    SHIFT_LEFT,
    SHIFT_RIGHT,
    SHIFT_UP,
    MovingAction,
    SpellAction,
)
from roguelike.algorithms.mob_decorator_confused import ConfusedDecorator
from roguelike.entities.abstract_object import AbstractObject
from roguelike.entities.user import User
from roguelike.map.map import GameMap
from roguelike.user_controller import UserController


@pytest.mark.parametrize(
    'action_type,method_name',
    [
        (SHIFT_UP, 'shift_up'),
        (SHIFT_DOWN, 'shift_down'),
        (SHIFT_LEFT, 'shift_left'),
        (SHIFT_RIGHT, 'shift_right'),
    ],
)
def test_moving_action(action_type, method_name):
    user_controller = MagicMock(spec=UserController)
    entity = MagicMock(spec=AbstractObject)

    action = MovingAction(action_type, entity, user_controller)
    action.run()

    method = getattr(user_controller, method_name)
    method.assert_called_once()


def test_spell_action_confused():
    game_map = MagicMock(spec=GameMap)
    user = MagicMock(spec=User)
    user.xcor.return_value = 5
    user.ycor.return_value = 5

    mob = MagicMock()
    mob.xcor.return_value, mob.ycor.return_value = 5, 6
    game_map.mobs = [mob]

    action = SpellAction(CONFUSED, game_map, user, 1)
    action.run()

    assert isinstance(mob.algo, ConfusedDecorator)
