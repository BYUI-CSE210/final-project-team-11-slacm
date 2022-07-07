import constants
import random

from game.scripting.action import Action
from game.shared.point import Point
from game.casting.car import Car
from game.shared.color import Color


class CreateCarAction(Action):
    """
    An action that creates cars

    The responsibility of CreatCarAction is to periodicially add a new car to the cast and set it moving in the correct direction.

    Attributes:
    ---

    """

    def __init__(self):
        """Constructs a new CreateCarAction.
        
        Args:
        ---
             """
        self._frame_counter = 0
        self._frame_interval = constants.SPAWN_INTERVAL

    def execute(self, cast, script):
        """Executes the create car action.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._frame_counter += 1
        if self._frame_counter % self._frame_interval == 0:
            self._new_car(cast)

    def _new_car(self, cast):
        """Creates a new car at either side of the screen.

        Args:
            cast (Cast): The cast of actors.
        """

        #randomly set row
        y = random.randint(1, constants.ROWS - 5) #from the top of the screen to just above the frog's start
         
        #if even row, start left move right
        if y % 2 == 0:
            x = 1
            velocity = Point(4, 0)
        #if odd row, start right move left
        else:
            x = constants.COLUMNS - 1
            velocity = Point(-4, 0)

        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        car = Car()

        car.set_color(color)
        car.set_position(position)
        car.set_velocity(velocity)
        #car.set_font_size(75) #this will require some playing with to do properly
        cast.add_actor("cars", car)