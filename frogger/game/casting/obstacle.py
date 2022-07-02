import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Obstacle(Actor):
    """
    An obstacle.
    
    The responsibility of Enemy is to move itsef across the window horizontally.

    Attributes:
        _points (int): The number of points the coin is worth.
    """
    def __init__(self):
        super().__init__()
