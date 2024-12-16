class StatsChange:
    """A class representing changes to an entity's stats.

    Attributes:
        damage (int): The change in damage value.
        health (int): The change in health value.
    """

    def __init__(self, damage: int, health: int):
        """Initialize a StatsChange instance.

        Args:
            damage (int): The change in damage value.
            health (int): The change in health value.
        """
        self.damage = damage
        self.health = health
