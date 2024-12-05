from random import randint

from algorithms.mob_algorithm import MobAlgorithm


class SimpleAlgo(MobAlgorithm):
    def __init__(self):

        self.possibles_ways = [self.shift_up, self.shift_down, self.shift_left, self.shift_right]

    def move(self, entity, map):
        x = randint(0, 3)
        self.possibles_ways[x](entity, map)

    def shift_up(self, entity, map):
        x = entity.xcor()
        y = entity.ycor() + map.move_size
        if map.check_walls(x, y):
            entity.goto(x, y)

    def shift_down(self, entity, map):
        x = entity.xcor()
        y = entity.ycor() - map.move_size
        if map.check_walls(x, y):
            entity.goto(x, y)

    def shift_left(self, entity, map):
        x = entity.xcor() - map.move_size
        y = entity.ycor()
        if map.check_walls(x, y):
            entity.goto(x, y)

    def shift_right(self, entity, map):
        x = entity.xcor() + map.move_size
        y = entity.ycor()
        if map.check_walls(x, y):
            entity.goto(x, y)

