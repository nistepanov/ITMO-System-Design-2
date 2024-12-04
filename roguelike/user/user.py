from typing import List

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Artifact:
    def __init__(self, artifact_id: int, bonus_type: str, bonus_value: int, coordinate: Coordinate):
        self.id = artifact_id
        self.bonus_type = bonus_type
        self.bonus_value = bonus_value
        self.coordinate = coordinate

class Artifact:
    def init(self, artifact_id: int, bonus_value: int, coordinate: Coordinate):
        self.id = artifact_id
        self.bonus_value = bonus_value
        self.coordinate = coordinate

class Armor(Artifact):
    def init(self, artifact_id: int, bonus_value: int, coordinate: Coordinate, defense: int):
        super().init(artifact_id, bonus_value, coordinate)
        self.defense = defense

class Weapon(Artifact):
    def init(self, artifact_id: int, bonus_value: int, coordinate: Coordinate, attack: int):
        super().init(artifact_id, bonus_value, coordinate)
        self.attack = attack


class User:

    _health: int
    _damage: int
    _speed: int
    _inventory: List[Artifact]
    _coordinate: Coordinate

    def __init__(self, health, damage, speed):
        self._health = health
        self._damage = damage
        self._speed = speed
        self._inventory = []
        self._coordinate = Coordinate(0, 0)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if value < 0:
            raise ValueError("Damage cannot be negative")
        self._damage = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative")
        self._speed = value

    @property
    def inventory(self):
        return self._inventory

    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, value):
        if not isinstance(value, Coordinate):
            raise ValueError("Coordinate must be a Coordinate object")
        self._coordinate = value
    
    def move(self, x, y):
        self._coordinate.x += x
        self._coordinate.y += y

    def check_death(self) -> bool:
        return self.health <= 0

    def equip(self, artifact: Artifact):
        if artifact not in self._inventory:
            self._inventory.append(artifact)
            if isinstance(artifact, Armor):
                self._health += artifact.bonus_value
            elif isinstance(artifact, Weapon):
                self._damage += artifact.bonus_value



    def unequip(self, artifact: Artifact):
        def unequip(self, artifact: Artifact):
        if artifact in self._inventory:
            self._inventory.remove(artifact)
            if isinstance(artifact, Armor):
                self._health -= artifact.bonus_value
            elif isinstance(artifact, Weapon):
                self._damage -= artifact.bonus_value
