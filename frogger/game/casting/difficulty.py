import constants


class Difficulty:
    """
    The difficulty setting for the game
    
    The responsibility of Difficulty is to track the velocities and spawn speeds of the cars.

    Attributes:
        _velocity (Point): The speed and direction.
        _spawn_timer (int): The number of frames in between each new car
        _increase (float): The number to increment the difficulty setting of the game
        
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
        if self._spawn_timer > 1:
            self._spawn_timer -= self._increase