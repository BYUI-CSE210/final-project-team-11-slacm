import constants


class Difficulty:
    """
    The difficulty setting for the game
    
    The responsibility of Difficulty is to track the velocities and spawn speeds of the cars.

    Attributes:
        _points (int): The number of points the coin is worth.
        
    """
    def __init__(self):
        self._velocity = constants.STARTING_VELOCITY
        self._spawn_timer = constants.SPAWN_INTERVAL
        self._increase = constants.DIFFICULTY_INCREASE

    def get_velocity(self):
        return int(self._velocity)

    def get_timer(self):
        return int(self._spawn_timer)

    def increase_difficulty(self):
        self._velocity += self._increase
        self._spawn_timer -= self._increase