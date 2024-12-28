from roguelike.algorithms.coward_algo import CowardAlgo
from roguelike.entities.dragon import Dragon
from roguelike.entities.simple_mob import SimpleMob
from roguelike.entities.skeleton import Skeleton
from roguelike.mob_factory.mob_factory import MobFactory


class CowardMobsFactory(MobFactory):
    """Factory for creating mobs with CowardAlgo."""

    def create_simple_mob(self) -> SimpleMob:
        """create_simple_mob logic.

        Returns:
            SimpleMob: Description of return value
        """
        return SimpleMob(CowardAlgo())

    def create_skeleton(self) -> Skeleton:
        """create_skeleton logic.

        Returns:
            Skeleton: Description of return value
        """
        mob = Skeleton(CowardAlgo())
        mob.health = 1  # Coward skeleton has lower health
        mob.damage = 1
        mob.speed(2)
        return mob

    def create_dragon(self) -> Dragon:
        """create_dragon logic.

        Returns:
            Dragon: Description of return value
        """
        return Dragon(CowardAlgo())
