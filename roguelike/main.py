import os

from roguelike import game


def main() -> None:
    """Main logic."""
    game_ = game.Game()
    game_.run()


if __name__ == '__main__':
    if os.environ.get('DISPLAY', '') == '':
        print('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')

    main()
