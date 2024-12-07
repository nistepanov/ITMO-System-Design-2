import turtle

from entities.abstract_object import AbstractObject


class Mob(AbstractObject):
    def __init__(self, algo):
        super().__init__()
        self.algo = algo

        turtle.register_shape(super().get_resources_path() + "/simple-mob.gif")
        self.shape(super().get_resources_path() + "/simple-mob.gif")
        self.health = 100
        self.attack = 10
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label():
        return "M"

    def move(self, map):
        self.algo.move(self, map)