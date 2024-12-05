import turtle

from entities.abstract_object import AbstractObject


class User(AbstractObject):
    def __init__(self, move_size):
        super().__init__()
        turtle.register_shape(super().get_resources_path() + "/hero.gif")
        self.shape(super().get_resources_path() + "/hero.gif")
        self.health = 300
        self.move_size = move_size
        self.attack = 10
        self.inventory = []
        self.experience = 0
        self.level = 1
        self.penup()
        self.speed(3)

    @staticmethod
    def get_label():
        return "P"

    def shift_up(self, map):
        x = self.xcor()
        y = self.ycor() + self.move_size
        if map.check_walls(x, y):
            self.goto(x, y)

    def shift_down(self, map):
        x = self.xcor()
        y = self.ycor() - self.move_size
        if map.check_walls(x, y):
            self.goto(x, y)

    def shift_left(self, map):
        x = self.xcor() - self.move_size
        y = self.ycor()
        if map.check_walls(x, y):
            self.goto(x, y)

    def shift_right(self, map):
        x = self.xcor() + self.move_size
        y = self.ycor()
        if map.check_walls(x, y):
            self.goto(x, y)

    def get_item(self, map):
        for i, item in enumerate(map.items):
            if item.xcor() == self.xcor() and item.ycor() == self.ycor():
                self.inventory.append(item)
                item.hideturtle()
                return

    def throw_item(self, map):
        item = self.inventory[0]
        self.inventory.remove(item)
        item.goto(self.xcor(), self.ycor())
        item.showturtle()
        map.items.append(item)


