import arcade
from game.constants import LIFE_SPACING, LIFE_POSITION_START, LIFE_COUNT

class Lives(arcade.Sprite):
    """
    A game booster that gives the player more chances to win all levels

    stereotype: information holder, life creator

    attributes: 
                self.center_x: positioning on the x axis
                self.center_y: positioning on the y axis
    """
    def __init__(self, center_x):
        """
        class constructor for lives

        args: 
            center_x: parameter that defines where to place the lives on the grid.
        """
        super().__init__(":resources:images/enemies/mouse.png", 0.25)
        self.center_x = center_x
        self.center_y = 20
