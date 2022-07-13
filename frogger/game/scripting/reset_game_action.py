import constants

from game.scripting.action import Action
from game.casting.cast import Cast
from game.casting.car import Car
from game.casting.coin import Coin
from game.casting.frog import Frog
from game.casting.lives import Lives
from game.casting.score import Score
from game.shared.point import Point


class ResetGameAction(Action):
    """
    An action that resets the game.
    
    The responsibility of ResetGameAction is to clear the players and reset their original states
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        #delete the original cast and game over message
        cars = cast.get_actors("cars")
        frog = cast.get_first_actor("frogs")
        live = cast.get_first_actor("lives")
        coins = cast.get_actors("coins")

        cast.remove_actor("frogs", frog)
        
        for coin in coins:
            cast.remove_actor("coins", coin)
        for car in cars:
            cast.remove_actor("cars", car) 

        #recreate the cast      
        cast.add_actor("coins", Coin())
        cast.add_actor("frogs", Frog())
        cast.add_actor("scores", Score())
        # cast.add_actor("cars", Car()) // removes the 'C' on top left of screen on game reset
        cast.add_actor("lives", Lives())
        
        position = Point(0, 0)
        live.set_position(position)
        live.set_position(Point(constants.MAX_X - 60, 0))
        live.set_position(Point(constants.MAX_X - 60, 0))
        lives = live.get_points()
        lives -= 1
        live.set_font_size(15)
        live.add_lives(-1)
        live.set_text(f"Lives: {lives}")

        