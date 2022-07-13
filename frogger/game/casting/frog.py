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
        self.set_position(position)
        self.set_color(Color(0, 255, 0))

    def move_next(self):
        """We're method overriding here to prevent movement if the frog attempts to move outside the maximum bounds of the screen."""

        if (
        (self._position.get_x() >= constants.MAX_X - constants.CELL_SIZE and self._velocity.get_x() > 0) #tries to run off right side of screen
        or (self._position.get_x() <= 0 and self._velocity.get_x() < 0) #tries to run off left side of screen
        or (self._position.get_y() >= constants.MAX_Y - constants.CELL_SIZE and self._velocity.get_y() > 0) #tries to run off bottom side of screen
        or (self._position.get_y() <= 0 and self._velocity.get_y() < 0) #tries to run off top side of screen
        ):
            return
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y())
        self._position = Point(x, y)