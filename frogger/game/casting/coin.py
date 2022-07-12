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
        _counter (int): The number of coins thus scored this game.
    """
    def __init__(self):
        "Constructs a new Coin."
        super().__init__()
        self._points = 0
        self.set_text("O")
        self.set_color(constants.YELLOW)
        self.reset()
        self._counter = 0
        
    def reset(self):
        """Selects a random position and points that the coin is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(8, constants.COLUMNS - 8)
        y = random.randint(4, constants.ROWS - 4)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the coin is worth.
        
        Returns:
            points (int): The points the coin is worth.
        """
        return self._points

    def get_counter(self):
        """Gets The number of coins thus scored this game.
        
        Returns:
            counter (int): The number of coins thus scored this game.
        """
        return self._counter

    def add_counter(self):
        """Upticks counter."""
        self._counter += 1