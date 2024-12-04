from typing import List


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
        self.attack = attac