import sched
import time
import turtle
import typing
from collections.abc import Callable
from queue import Queue
from random import randint

from roguelike.action.action_entity import (
    ACTIVATE_ITEM,
    CONFUSED,
    DEACTIVATE_ITEM,
    GET_ITEM,
    SHIFT_DOWN,
    SHIFT_LEFT,
    SHIFT_RIGHT,
    SHIFT_UP,
    ItemAction,
    MovingAction,
    SpellAction,
)
from roguelike.entities.copy_mob import CopyMob
from roguelike.entities.mob import Mob
from roguelike.map import map, map_builder
from roguelike.user_controller import UserController


EXIT_DELAY = 750

DEFAULT_RESIST_TIME = 50


class Game:
    """Game logic."""

    def __init__(self) -> None:
        self.game_width = 1500
        self.game_height = 1200
        turtle.setup(self.game_width, self.game_height)
        self.window = turtle.Screen()
        self.move_size = 64
        self.is_running = True
        self.map: map.GameMap = (
            map_builder.MapBuilder(window=self.window)
            .set_map_size(rows=10, columns=20)
            .set_start_position(start_x=640, start_y=200)
            .set_block_size(block_size=self.move_size)
            .build()
        )
        self.priority_queue: Queue = Queue()
        self.user = self.map.user
        self.user_controller = UserController(self.user, self.map, self.move_size)

        turtle.listen()
        turtle.onkey(self.shift_left, 'Left')
        turtle.onkey(self.shift_right, 'Right')
        turtle.onkey(self.shift_down, 'Down')
        turtle.onkey(self.shift_up, 'Up')
        turtle.onkey(self.get_item, 'i')
        turtle.onkey(self.get_item, 'I')
        turtle.onkey(self.confused, 'c')
        turtle.onkey(self.confused, 'C')
        for i in range(1, 7):
            turtle.onkey(self.activate_item(i), str(i))

        turtle.onkey(self.deactivate_item(1), 'q')
        turtle.onkey(self.deactivate_item(1), 'Q')
        turtle.onkey(self.deactivate_item(2), 'w')
        turtle.onkey(self.deactivate_item(2), 'W')
        turtle.onkey(self.deactivate_item(3), 'e')
        turtle.onkey(self.deactivate_item(3), 'E')

    def deactivate_item(self, i: int) -> Callable[[], None]:
        """deactivate_item logic."""
        return lambda: self.priority_queue.put(
            ItemAction(type=DEACTIVATE_ITEM, id=i - 1, user_controller=self.user_controller)
        )

    def confused(self) -> None:
        """deactivate_item logic."""
        self.priority_queue.put(SpellAction(type=CONFUSED, map=self.map, user=self.user, move_size=self.move_size))

    def activate_item(self, i: int) -> Callable[[], None]:
        """activate_item logic."""
        return lambda: self.priority_queue.put(
            ItemAction(type=ACTIVATE_ITEM, id=i - 1, user_controller=self.user_controller)
        )

    def get_item(self) -> None:
        """get_item logic."""
        self.priority_queue.put(ItemAction(type=GET_ITEM, id=0, user_controller=self.user_controller))

    def shift_up(self) -> None:
        """shift_up logic."""
        self.priority_queue.put(MovingAction(type=SHIFT_UP, entity=self.user, user_controller=self.user_controller))

    def shift_down(self) -> None:
        """shift_down logic."""
        self.priority_queue.put(MovingAction(type=SHIFT_DOWN, entity=self.user, user_controller=self.user_controller))

    def shift_left(self) -> None:
        """shift_left logic."""
        self.priority_queue.put(MovingAction(type=SHIFT_LEFT, entity=self.user, user_controller=self.user_controller))

    def shift_right(self) -> None:
        """shift_right logic."""
        self.priority_queue.put(MovingAction(type=SHIFT_RIGHT, entity=self.user, user_controller=self.user_controller))

    def run(self) -> None:
        """Run logic.

        Returns:
            None:
        """
        self.is_running = True
        has_resist = 0
        s = sched.scheduler(time.time, time.sleep)
        for mob in self.map.mobs:
            if isinstance(mob, CopyMob):
                s.enterabs(10, 1, self.clone(mob))
        s.run()
        while self.is_running:
            if has_resist > 0:
                has_resist -= 1
            if not self.user.alive:
                self.window.ontimer(self.window.bye, EXIT_DELAY)
            for mob in self.map.mobs:
                if randint(0, 20) == 0:
                    moving = mob.move(self.map)
                    if moving is None:
                        continue
                    (x, y) = moving
                    if has_resist == 0 and self.map.is_user(x, y):
                        self.battle_with_mob(mob=mob)
                        has_resist = DEFAULT_RESIST_TIME
                    else:
                        mob.goto(x, y)

            has_resist = self.process_queue(has_resist)
            self.window.update()
        self.window.bye()

    def clone(self, mob: CopyMob) -> typing.Any:
        """Clone logic.

        Args:
            mob (CopyMob): Description of mob.

        Returns:
            typing.Any: Description of return value
        """
        return lambda: self.map.mobs.append(mob.clone())

    def process_queue(self, has_resist: int) -> int:
        """Command queue processing."""
        while self.priority_queue.qsize() > 0 and self.user.alive:
            self.priority_queue.get().run()
            for mob in self.map.mobs:
                if has_resist == 0 and mob.xcor() == self.user.xcor() and mob.ycor() == self.user.ycor():
                    self.battle_with_mob(mob=mob)
                    has_resist = DEFAULT_RESIST_TIME
        return has_resist

    def battle_with_mob(self, mob: Mob) -> None:
        """Function with battle logic."""
        mob.health -= self.user.damage
        self.user_controller.update_health(-mob.damage)
        if mob.health <= 0:
            mob.hideturtle()
            self.user_controller.update_xp(5)

    def get_walls(self) -> list[tuple[int, int]]:
        """Walls getter.

        Returns:
            list[tuple[int, int]]: Description of return value
        """
        return self.map.walls
