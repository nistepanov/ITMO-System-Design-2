import random

from roguelike.entities.copy_mob import CopyMob
from roguelike.entities.dragon import Dragon
from roguelike.entities.mob import Mob
from roguelike.entities.simple_mob import SimpleMob
from roguelike.entities.skeleton import Skeleton


class MobFactory:
    """Interface for mob factories."""

    def create_simple_mob(self) -> SimpleMob:
        """create_simple_mob logic.

        Returns:
            SimpleMob: Description of return value
        """
        raise NotImplementedError

    def create_skeleton(self) -> Skeleton:
        """create_skeleton logic.

        Returns:
            Skeleton: Description of return value
        """
        raise NotImplementedError

    def create_dragon(self) -> Dragon:
        """create_dragon logic.

        Returns:
            Dragon: Description of return value
        """
        raise NotImplementedError

    def create_copy_mob(self) -> CopyMob:
        """create_copy_mob logic.

        Returns:
            CopyMob: Description of return value
        """
        raise NotImplementedError

    def create_random_mob(self) -> Mob:
        """create_random_mob logic.

        Returns:
            Mob: Description of return value
        """
        mob_type = random.choice([
            self.create_simple_mob,
            self.create_skeleton,
            self.create_dragon,
            self.create_copy_mob,
        ])
        return mob_type()
