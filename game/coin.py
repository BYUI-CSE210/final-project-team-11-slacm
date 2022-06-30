import arcade
from game.constants import SPRITE_SCALING_COIN
import random
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Coin(arcade.Sprite):
    """
    Creates a coin sprite

    attributes:
                self.coin(None)
                self.coin_list(None)
                self(arcade.Sprite): an instance of Sprite
                self.center_x: random positioning on the x coordinates
                self.center_y: random positioning on the y coordinates


    """
    def __init__(self):
        self.coin = None
        self.coin_list = None
        super().__init__(":resources:images/items/star.png", SPRITE_SCALING_COIN)
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)
