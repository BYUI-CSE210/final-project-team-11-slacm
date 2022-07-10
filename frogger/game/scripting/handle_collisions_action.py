import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.car import Car

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the frog collides
    with the coins, or the frog collides with the obstacles, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_coin_collision(cast)
            self._handle_obstacle_collision(cast)
            #self._handle_game_over(cast)
        else:
            self._handle_game_over(cast)
            

    def _handle_coin_collision(self, cast):
        """Updates the score and moves the coin if the frog collides with the coin.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        coins = cast.get_actors("coins")
        frog = cast.get_first_actor("frogs")

        frog_x = frog.get_position().get_x()
        frog_y = frog.get_position().get_y()
        
        for coin in coins:

            coin_x = coin.get_position().get_x()
            coin_y = coin.get_position().get_y()

            if ((coin_x - constants.FONT_SIZE/2 < frog_x < coin_x + constants.FONT_SIZE/2) and (coin_y - constants.FONT_SIZE/2 < frog_y < coin_y + constants.FONT_SIZE/2)):
                points = coin.get_points()
                score.add_points(points)
                coin.reset()
    
    def _handle_obstacle_collision(self, cast):
        """Sets the game over flag if the frog collides with one of the obstacles.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        
        
        cars = cast.get_actors("cars")
        frog = cast.get_first_actor("frogs")

        frog_x = frog.get_position().get_x()
        frog_y = frog.get_position().get_y()
        
        for car in cars:

            car_x = car.get_position().get_x()
            car_y = car.get_position().get_y()

            if ((car_x - constants.FONT_SIZE/2 < frog_x < car_x + constants.FONT_SIZE/2) and (car_y - constants.FONT_SIZE/2 < frog_y < car_y + constants.FONT_SIZE/2)):
                self._is_game_over = True
        

        


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and the final score if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        

        """
        score = cast.get_first_actor("scores")

        score.set_text(f"GAME OVER Score: {score._points}")
        
        