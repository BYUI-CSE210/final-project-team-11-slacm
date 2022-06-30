import arcade
from game.constants import SPRITE_SCALING, SCREEN_WIDTH, SCREEN_HEIGHT
import os


class Player(arcade.Sprite):
    """
    A sprite that moves throughout the level and tries to avoid getting hit by the cars

    stereotype: information holder, player creator

    attributes: 
                self.center_x: positioning on the x axis in the center
                self.center_y: positioning on the y axis at the bottom
    """
    def __init__(self):
        """
        class constructor

        """
        super().__init__(":resources:images/enemies/mouse.png", SPRITE_SCALING)

        self.center_x = 400
        self.center_y = 50

    def update(self):

        """ 
        update information about the player such as the changes in speed, direction, and boundries
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0

        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0

        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1