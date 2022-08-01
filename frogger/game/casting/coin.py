import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Coin(Actor):
    """
    A coin the car can collect to obtain additional points.
    
    The responsibility of Coin is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the coin is worth.
    """
    def __init__(self):
        "Constructs a new Coin."
        super().__init__()
        self._points = 0
        self.set_text("O")
        self.set_color(constants.YELLOW)
        self.reset()
        self._font_size = constants.CELL_SIZE*2
        
    def reset(self):
        """Selects a random position and points that the coin is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(4, constants.COLUMNS/2 - 4)
        y = random.randint(2, constants.ROWS/2 - 2)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE*2)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the coin is worth.
        
        Returns:
            points (int): The points the coin is worth.
        """
        return self._points