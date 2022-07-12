from game.scripting.action import Action
from game.shared.point import Point


class ControlFrogAction(Action):
    """
    An input action that controls the frog.
    
    The responsibility of ControlFrogAction is to get the direction and move the frog.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlFrogAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        self._direction = self._keyboard_service.get_direction()
        frog = cast.get_first_actor("frogs")
        frog.set_velocity(self._direction)