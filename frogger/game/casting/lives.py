import constants
from game.casting.actor import Actor
from game.shared.point import Point



class Lives(Actor):
    def __init__(self):
        super().__init__()
        self._lives = 0
        self.add_lives(3)
        position = Point(0, 0)
        self.set_position(position)
        self.set_position(Point(constants.MAX_X - 50, 0))

    def add_lives(self, lives):
        """Adds the given lives to the total lives.
        
        Args:
            points (int): The points to add.
        """
        self._lives += lives
        self.set_text(f"Life: {self._lives}")

    def get_points(self):
        """Sets lifes for the player
        Returns:
        ---
            Integer: A point value for each player.
        """
        return self._lives

    def reduce_lives(self):
        """Reduces lives for the player"""
        self._lives -= 1
        self.set_text(f"Lives: {self._lives}")


