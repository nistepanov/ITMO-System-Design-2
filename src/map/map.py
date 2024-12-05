class GameMap:
    def __init__(self, walls, mobs, items, user, move_size):
        self.walls = walls
        self.mobs = mobs
        self.items = items
        self.user = user
        self.move_size = move_size

    def check_walls(self, x, y):
        return not((x, y) in self.walls)

