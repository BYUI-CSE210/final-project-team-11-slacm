import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Frog(Actor):
    """
    A frog.
    
    The responsibility of Frog is to move.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self.set_text("F")
        self.set_font_size(50)
        position = Point(int(constants.MAX_X / 2), int(constants.MAX_Y -constants.CELL_SIZE*2))

        #position = Point(constants.COLUMNS-1, constants.ROWS-1)
        #position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        

"""
    def move_next(self):

        pass
    """