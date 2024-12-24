from roguelike.algorithms.agressive_algo import AgressiveAlgo
from roguelike.entities.dragon import Dragon
from roguelike.entities.simple_mob import SimpleMob
from roguelike.entities.skeleton import Skeleton
from roguelike.mob_factory.mob_factory import MobFactory


class AggressiveMobsFactory(MobFactory):
    """Factory for creating mobs with AggressiveAlgo."""

    def create_simple_mob(self) -> SimpleMob:
        """create_simple_mob logic.

        Returns:
            SimpleMob: Description of return value
        """
        mob = SimpleMob(AgressiveAlgo())
        mob.health = 4  # Aggressive simple mob is stronger and faster
        mob.damage = 2
        mob.speed(4)
        return mob

    def create_skeleton(self) -> Skeleton:
        """create_skeleton logic.

        Returns:
            Skeleton: Description of return value
        """
        mob = Skeleton(AgressiveAlgo())
        mob.health = 3  # Aggressive skeleton has higher health
        mob.damage = 2
        mob.speed(3)
        return mob

    def create_dragon(self) -> Dragon:
        """create_dragon logic.

        Returns:
            Dragon: Description of return value
        """
        mob = Dragon(AgressiveAlgo())
        mob.health = 6  # Aggressive dragon is weaker
        mob.damage = 2
        mob.speed(2)
        return mob
