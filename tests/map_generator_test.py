from unittest.mock import Mock

import pytest

from roguelike.map import map_generator


@pytest.fixture
def mock_window():
    """Provide a mock window object for testing."""
    return Mock()


@pytest.fixture
def _map_generator(mock_window):
    """Create a MapGenerator instance for tests."""
    return map_generator.MapGenerator(window=mock_window, rows=10, columns=10, start_x=0, start_y=0, bl_size=20)


def test_initial_grid_structure(_map_generator):
    """Test the initial structure of the map."""
    grid = _map_generator.grid
    rows, cols = len(grid), len(grid[0])

    # Ensure grid dimensions match the specified size.
    assert rows == 10
    assert cols == 10

    # Verify that the edges are filled with walls.
    for i in range(rows):
        assert grid[i][0] == '#'
        assert grid[i][cols - 1] == '#'
    for j in range(cols):
        assert grid[0][j] == '#'
        assert grid[rows - 1][j] == '#'

    # Verify that the interior is filled with dots.
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            assert grid[i][j] == '.'


def test_generate_random_walls(_map_generator):
    """Test the generation of random walls."""
    _map_generator.generate_random_walls()
    grid = _map_generator.grid

    # Ensure the grid contains at least one random wall.
    inner_cells = [grid[i][j] for i in range(1, len(grid) - 1) for j in range(1, len(grid[0]) - 1)]
    assert '#' in inner_cells


def test_generate_random_enemies(_map_generator):
    """Test the generation of random enemies."""
    _map_generator.generate_random_enemies()
    grid = _map_generator.grid

    # Ensure the grid contains at least one enemy.
    inner_cells = [grid[i][j] for i in range(1, len(grid) - 1) for j in range(1, len(grid[0]) - 1)]
    assert 'M' in inner_cells


def test_generate_random_items(_map_generator):
    """Test the generation of random items."""
    _map_generator.generate_random_items()
    grid = _map_generator.grid

    # Ensure the grid contains at least one item (weapon or shield).
    inner_cells = [grid[i][j] for i in range(1, len(grid) - 1) for j in range(1, len(grid[0]) - 1)]
    assert 'W' in inner_cells or 'S' in inner_cells


def test_generate_random_user(_map_generator):
    """Test the generation of the player's position."""
    _map_generator.generate_random_user()
    grid = _map_generator.grid

    # Ensure the player is located on the map.
    user_positions = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'U']
    assert len(user_positions) == 1  # The player should be unique.


def test_create_map_raises_exception_if_elements_missing(_map_generator):
    """Test that an exception is raised if necessary elements are missing."""
    # Create a MapGenerator with a grid that is guaranteed to lack necessary elements.
    # Clear the grid to ensure it contains no walls, enemies, items, or the player.
    _map_generator.grid = [['.' for _ in range(5)] for _ in range(5)]
    # Ensure that calling create_map raises a MapGeneratorException.
    with pytest.raises(map_generator.MapGeneratorException):
        _map_generator.create_map(skip_generate=True)
