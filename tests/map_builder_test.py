import os
from unittest.mock import MagicMock, patch

import pytest

from roguelike.entities.artifact import Shield, Weapon
from roguelike.entities.image import Image
from roguelike.entities.inventory_slot import InventorySlot
from roguelike.entities.mob import Mob
from roguelike.entities.text_object import TextObject
from roguelike.entities.user import User
from roguelike.entities.wall import Wall
from roguelike.inventory.inventory import Inventory
from roguelike.map.map import GameMap
from roguelike.map.map_builder import MapBuilder, MapBuilderException


@pytest.fixture(autouse=True)
def setup_tkinter_envs():
    current_display = os.environ.get('DISPLAY')
    os.environ['DISPLAY'] = f'unix{current_display}'


@pytest.fixture
def mock_window():
    window = MagicMock()
    return window


@pytest.fixture
def map_builder(mock_window):
    return MapBuilder(mock_window)


def test_set_map_size(map_builder):
    builder = map_builder.set_map_size(20, 30)
    assert builder.rows == 20
    assert builder.columns == 30


def test_set_start_position(map_builder):
    builder = map_builder.set_start_position(100, 150)
    assert builder.start_x == 100
    assert builder.start_y == 150


def test_set_block_size(map_builder):
    builder = map_builder.set_block_size(50)
    assert builder.bl_size == 50


def test_load_map_from_file(map_builder):
    builder = map_builder.load_map_from_file('test_map.txt')
    assert builder.load_from_file is True
    assert builder.file_path == 'test_map.txt'


def test_load_map_from_file_none_path(map_builder):
    with pytest.raises(MapBuilderException, match='MapBuilder: file_path is None'):
        map_builder.load_map_from_file(None)


@patch('roguelike.map.map_builder.open', new_callable=MagicMock, create=True)
def test_load_map_from_file_content(mock_open, map_builder):
    mock_file = MagicMock()
    mock_file.__iter__.return_value = ['#W.\n', '.M#\n', 'U.S\n']
    mock_open.return_value.__enter__.return_value = mock_file
    map_builder.load_map_from_file('test_map.txt')
    map_builder._load_map_from_file()
    assert map_builder.grid == [['#', 'W', '.'], ['.', 'M', '#'], ['U', '.', 'S']]


def test_load_map_from_file_no_path_on_build(map_builder):
    map_builder.load_from_file = True
    with pytest.raises(MapBuilderException, match='File path must be provided to load the map.'):
        map_builder.build()


@patch('roguelike.map.map_builder.open', new_callable=MagicMock, create=True)
@patch.object(Wall, 'goto')
@patch.object(Weapon, 'goto')
@patch.object(Shield, 'goto')
@patch.object(User, 'goto')
@patch.object(Mob, 'goto')
@patch.object(InventorySlot, 'goto')
@patch.object(TextObject, 'goto')
@patch.object(MapBuilder, '_generate_inventory')
@patch.object(MapBuilder, '_generate_stats')
def test_build_load_map(
    mock_generate_stats,
    mock_generate_inventory,
    mock_text_goto,
    mock_inventory_goto,
    mock_mob_goto,
    mock_user_goto,
    mock_shield_goto,
    mock_weapon_goto,
    mock_wall_goto,
    mock_open,
    map_builder,
    mock_window,
):
    mock_file = MagicMock()
    mock_file.__iter__.return_value = ['#W.\n', '.M#\n', 'U.S\n']
    mock_open.return_value.__enter__.return_value = mock_file
    map_builder.load_map_from_file('test_map.txt')
    mock_generate_inventory.return_value = MagicMock(spec=Inventory)
    game_map = map_builder.build()

    assert isinstance(game_map, GameMap)
    assert len(game_map.walls) > 0
    assert len(game_map.items) > 0
    assert len(game_map.mobs) > 0
    assert isinstance(game_map.user, User)
    assert isinstance(game_map.inventory, Inventory)
    assert game_map.move_size == map_builder.bl_size

    assert mock_user_goto.call_count == 1
    assert mock_mob_goto.call_count == 1
    mock_window.tracer.assert_called_once_with(0)
    mock_window.update.assert_called()


@patch.object(InventorySlot, 'write')
def test_generate_inventory(mock_write, map_builder):
    inventory = map_builder._generate_inventory()
    assert isinstance(inventory, Inventory)
    assert len(inventory.inventory) == 6
    assert len(inventory.active_items) == 3
    assert mock_write.call_count == 9  # 3 for active, 6 for inventory


@patch.object(TextObject, 'write')
@patch.object(Image, 'goto')
def test_generate_stats(mock_image_goto, mock_text_write, map_builder):
    map_builder._generate_stats()
    assert isinstance(map_builder.experience_slot, TextObject)
    assert isinstance(map_builder.weapon_slot, TextObject)
    assert isinstance(map_builder.shield_slot, TextObject)
    assert mock_text_write.call_count == 3
    mock_text_write.assert_any_call(str(MapBuilder._USER_LEVEL), align='center', font=map_builder.data_font)
    mock_text_write.assert_any_call(str(MapBuilder._USER_DAMAGE), align='center', font=map_builder.data_font)
    mock_text_write.assert_any_call(str(MapBuilder._USER_HEALTH), align='center', font=map_builder.data_font)
    assert mock_image_goto.call_count == 3


@patch('roguelike.map.map_builder.randint', return_value=0)
def test_get_mob(mock_randint, map_builder):
    mob = map_builder._get_mob()
    assert isinstance(mob, Mob)
