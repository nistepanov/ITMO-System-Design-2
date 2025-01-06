from unittest.mock import MagicMock

from roguelike.algorithms import passive_algo
from roguelike.entities.mob import Mob
from roguelike.state.bravery_state import BraveryState
from roguelike.state.default_state import DefaultState
from roguelike.state.panic_state import PanicState


def test_default_state_to_panic():
    """Test transition from DefaultState to PanicState."""
    entity = Mob
    entity.health = 5
    entity.maxHealth = 10
    entity.algo = passive_algo.PassiveAlgo

    game_map = MagicMock()

    res = DefaultState.move(entity, game_map)
    assert res is None
    assert entity.state == PanicState


def test_panic_state_to_default():
    """Test transition from DefaultState to BraveryState."""

    entity = Mob
    entity.health = 9
    entity.maxHealth = 10
    entity.algo = passive_algo.PassiveAlgo

    game_map = MagicMock()

    res = PanicState.move(entity, game_map)
    assert res is None
    assert entity.state == DefaultState


def test_bravery_state_to_default():
    entity = Mob
    entity.health = 9
    entity.maxHealth = 10
    entity.algo = passive_algo.PassiveAlgo

    game_map = MagicMock()

    res = BraveryState.move(entity, game_map)
    assert res is None
    assert entity.state == DefaultState
