import abc


class BaseEnemy(abc.ABC):
    """BaseEnemy logic."""

    def __init__(
        self,
        enemy_id: int,
        health: int,
        damage: int,
        speed: int,
        vision_range: int,
        coordinates: tuple[int, int],
    ):
        self.id = enemy_id
        self._health = health
        self._damage = damage
        self._speed = speed
        self._vision_range = vision_range
        self._coordinates = coordinates

    @abc.abstractmethod
    def move(self) -> None:
        """Move logic.

        Returns:
            None: Description of return value
        """
        pass

    @abc.abstractmethod
    def attack_player(self) -> None:
        """attack_player logic.

        Returns:
            None: Description of return value
        """
        pass

    @abc.abstractmethod
    def die(self) -> None:
        """Die logic.

        Returns:
            None: Description of return value
        """
        pass
