from roguelike.algorithms.passive_algo import PassiveAlgo
from roguelike.entities.dragon import Dragon
from roguelike.entities.simple_mob import SimpleMob
from roguelike.entities.skeleton import Skeleton
from roguelike.mob_factory.mob_factory import MobFactory


class PassiveMobsFactory(MobFactory):
    """Factory for creating mobs with PassiveAlgo."""

    def create_simple_mob(self) -> SimpleMob:
        """create_simple_mob logic.

        Returns:
            SimpleMob: Description of return value
        """
        return SimpleMob(PassiveAlgo())

    def create_skeleton(self) -> Skeleton:
        """create_skeleton logic.

        Returns:
            Skeleton: Description of return value
        """
        mob = Skeleton(PassiveAlgo())
        mob.health = 3  # Passive skeleton has more health
        mob.maxHealth = mob.health
        mob.damage = 1
        return mob

    def create_dragon(self) -> Dragon:
        """create_dragon logic.

        Returns:
            Dragon: Description of return value
        """
        mob = Dragon(PassiveAlgo())
        mob.health = 15  # Passive dragon has more health, but almost have no damage
        mob.maxHealth = mob.health
        mob.damage = 1
        return mob
