import turtle
from queue import PriorityQueue
from random import randint

from map.map_generator import MapGenerator


class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.move_size = 64
        self.is_running = True
        self.map = MapGenerator(self.window, 10, 20, 640, 320, self.move_size).create_map()
        self.priority_queue = PriorityQueue()
        self.user = self.map.user

        turtle.listen()
        turtle.onkey(self.shift_left, "Left")
        turtle.onkey(self.shift_right, "Right")
        turtle.onkey(self.shift_down, "Down")
        turtle.onkey(self.shift_up, "Up")
        turtle.onkey(self.get_item, "i")
        turtle.onkey(self.get_item, "I")
        turtle.onkey(self.throw_item, "t")
        turtle.onkey(self.throw_item, "T")


    def shift_up(self):
        self.user.shift_up(self.map)

    def shift_down(self):
        self.user.shift_down(self.map)

    def shift_left(self):
        self.user.shift_left(self.map)

    def shift_right(self):
        self.user.shift_right(self.map)

    def get_item(self):
        self.user.get_item(self.map)


    def throw_item(self):
        self.user.throw_item()

    def run(self):
        self.is_running = True
        while self.is_running:

            for mob in self.map.mobs:
                rand = randint(0, 20)
                if rand == 0:
                    mob.move(self.map)
            self.window.update()

        self.window.bye()

    def get_walls(self):
        return self.map.walls

