import constants
from game.shared.point import Point
from game.casting.actor import Actor



class Lives(Actor):
    def __init__(self):
        super().__init__()
        self._lifes = 0
        self.add_lives(3)

    def add_lives(self, lifes):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._lifes += lifes
        self.set_text(f"Life: {self._lifes}")

    def get_points(self):
        """Sets points for the user

        Returns:
        ---
            Integer: A point value for each player.
        """
        return self._lifes

    def reduce_lives(self):
        """Reduces points for the user"""
        self._lifes -= 1
        self.set_text(f"Lives: {self._lifes}")


