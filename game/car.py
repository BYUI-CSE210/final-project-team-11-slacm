import arcade
from arcade.key import Y
from arcade.sprite import PyMunk
from game.constants import CAR_SPRITE_SCALING, SCREEN_HEIGHT, SCREEN_WIDTH, PICTURES_PATH, Y_SPACING
import random


class Car(arcade.Sprite):
    """ A car that will keep track of its velocity, and positioning in the game.

    Attributes:
        center_y: positioning in the game's y axis
        center_x: positioning in teh game's x axis
        change_x: sets the velocity for the car
    """
    def __init__(self, center_y, velocity):
        """ The class constructor.

        args: 
            center_y: positioning in the game's y axis
            velocity: speed and direction the car is moving
        """
        super().__init__((PICTURES_PATH + "car.png"), CAR_SPRITE_SCALING)
        self.change_x = velocity
        self.center_y = center_y
        self.center_x = random.randint(0, SCREEN_WIDTH)

    def update(self):
        """
        updates the important information for the cars repositioning
        """
        if self.left > SCREEN_WIDTH:
            self.center_x = 0
        elif self.right < 0:
            self.center_x = 800

        return super().update()

