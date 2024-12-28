from roguelike.entities.abstract_object import AbstractObject


class TextObject(AbstractObject):
    """Text logic."""

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()

    @staticmethod
    def get_label() -> str:
        """get_label logic.

        Returns:
            str: Description of return value
        """
        return 'EM'
