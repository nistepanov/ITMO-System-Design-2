import os
from unittest.mock import MagicMock, patch

import pytest

from roguelike.map.map_builder import MapBuilder, MapBuilderException


@pytest.fixture(autouse=True)
def setup_tkinter_envs():
    os.environ.__setitem__('DISPLAY', 'localhost')


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
