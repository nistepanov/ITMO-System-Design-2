import turtle
from queue import PriorityQueue
from random import randint

from roguelike.map import map, map_generator
from roguelike.user_controller import UserController


class Game:
    """Game logic."""

    def __init__(self) -> None:
        self.game_width = 1500
        self.game_height = 1200
        turtle.setup(self.game_width, self.game_height)
        self.window = turtle.Screen()
        self.move_size = 64
        self.is_running = True
        self.map: map.GameMap = map_generator.MapGenerator(
            window=self.window,
            rows=10,
            columns=20,
            start_x=640,
            start_y=200,
            bl_size=self.move_size,
        ).create_map()
        self.priority_queue: PriorityQueue = PriorityQueue()
        self.user = self.map.user
        self.user_controller = UserController(self.user, self.map, self.move_size)

        turtle.listen()
        turtle.onkey(self.shift_left, 'Left')
        turtle.onkey(self.shift_right, 'Right')
        turtle.onkey(self.shift_down, 'Down')
        turtle.onkey(self.shift_up, 'Up')
        turtle.onkey(self.get_item, 'i')
        turtle.onkey(self.get_item, 'I')
        for i in range(1, 6):
            turtle.onkey(self.activate_item(i), str(i))

        turtle.onkey(self.throw_item(1), 'q')
        turtle.onkey(self.throw_item(1), 'Q')
        turtle.onkey(self.throw_item(2), 'w')
        turtle.onkey(self.throw_item(2), 'W')
        turtle.onkey(self.throw_item(3), 'e')
        turtle.onkey(self.throw_item(3), 'E')


    def throw_item(self, i):
        return lambda: self.user_controller.throw_item(i - 1)

    def activate_item(self, i):
        return lambda: self.user_controller.activate_item(i - 1)

    def shift_up(self) -> None:
        """shift_up logic."""
        self.user_controller.shift_up(self.map)

    def shift_down(self) -> None:
        """shift_down logic."""
        self.user_controller.shift_down(self.map)

    def shift_left(self) -> None:
        """shift_left logic."""
        self.user_controller.shift_left(self.map)

    def shift_right(self) -> None:
        """shift_right logic."""
        self.user_controller.shift_right(self.map)

    def get_item(self) -> None:
        """get_item logic."""
        self.user_controller.get_item(self.map)

    def run(self) -> None:
        """Run logic.

        Returns:
            None:
        """
        self.is_running = True
        while self.is_running:
            for mob in self.map.mobs:
                rand = randint(0, 20)
                if rand == 0:
                    mob.move(self.map)
            self.window.update()
        self.window.bye()

    def get_walls(self) -> list[tuple[int, int]]:
        """get_walls logic.

        Returns:
            list[tuple[int, int]]: Description of return value
        """
        return self.map.walls
