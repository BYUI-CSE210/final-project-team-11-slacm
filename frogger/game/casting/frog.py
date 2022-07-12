import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Frog(Actor):
    """
    A frog.
    
    The responsibility of Frog is to move.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self.set_text("F")
        position = Point(int(constants.MAX_X / 2), int(constants.MAX_Y -constants.CELL_SIZE*2))

        #position = Point(constants.COLUMNS-1, constants.ROWS-1)
        #position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        self.set_color(Color(0, 255, 0))