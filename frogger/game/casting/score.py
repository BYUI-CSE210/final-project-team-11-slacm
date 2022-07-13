from game.casting.actor import Actor
import constants

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by crossing the road and collecting coins.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _threshold (int): The amount of points needed per additonal life earned.
    """
    def __init__(self):
        super().__init__()
        self._threshold = constants.LIFE_THRESHOLD
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def reset_points (self):
        """Reset points to 0.       
        """

        self.points = 0

    def get_score (self):
        """Gets the points the coin is worth.
        
        Returns:
            points (int): The points earned in the game.
        """
        return self._points

    def check_threshold (self):
        if self._points >= self._threshold:
            self._threshold += constants.LIFE_THRESHOLD
            return True
        else:
            return False