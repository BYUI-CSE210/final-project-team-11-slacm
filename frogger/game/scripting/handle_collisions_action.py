import constants
from game.scripting.action import Action
from game.scripting.reset_game_action import ResetGameAction
from game.services.keyboard_service import KeyboardService
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the frog collides
    with the coins, or the frog collides with the obstacles, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
        _difficulty (Difficulty): An instance of Difficulty.
 """

    def __init__(self, difficulty):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._difficulty = difficulty

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_coin_collision(cast)
            self._handle_obstacle_collision(cast)
        else:
            self._handle_game_over(cast, script)
            

    def _handle_coin_collision(self, cast):
        """Updates the score and moves the coin if the frog collides with the coin.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        coins = cast.get_actors("coins")
        frog = cast.get_first_actor("frogs")
        lives = cast.get_first_actor("lives")

        frog_x = frog.get_position().get_x()
        frog_y = frog.get_position().get_y()
        
        for coin in coins:

            coin_x = coin.get_position().get_x()
            coin_y = coin.get_position().get_y()

            if ((coin_x - constants.FONT_SIZE/2 < frog_x < coin_x + constants.FONT_SIZE/2) and (coin_y - constants.FONT_SIZE/2 < frog_y < coin_y + constants.FONT_SIZE/2)):
                points = coin.get_points()
                score.add_points(points)
                coin.add_counter()
                if coin.get_counter() % constants.COINS_PER_LIFE == 0:
                    lives.add_lives(1)
                coin.reset()
                self._difficulty.increase_difficulty()

    
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

            #if car is off-screen, kill it
            if car_x > constants.MAX_X + constants.CAR_CELL_SIZE or car_x < -constants.CAR_CELL_SIZE:
                cast.remove_actor("cars", car)

            #if car hits player, game over
            if ((car_x - constants.CELL_SIZE/2 < frog_x < car_x + constants.CAR_CELL_SIZE - constants.CELL_SIZE) and (car_y - constants.CELL_SIZE < frog_y < car_y + constants.CAR_CELL_SIZE)):
                self._is_game_over = True
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and the final score if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.

        """
 
        x = int(constants.MAX_X / 3)
        y = int(constants.MAX_Y / 3)
        position = Point(x, y) 
        live = cast.get_first_actor("lives")
        lives = live.get_points()
        live.reduce_lives(-1)
        
        self._keyboard_service = KeyboardService()
        if lives > 0:
            live.set_position(position)
            live.set_font_size(30)
            live.set_text(f"{lives} lives left.\nPress Spacebar to Reset")
            if self._keyboard_service.is_key_down(' '):
                    reset = ResetGameAction()
                    reset.execute(cast, script)
                    self._is_game_over = False
        if lives == 0:
            live.reset_lives()
            live.set_position(position)
            live.set_font_size(50)
            live.set_text(f"GAME OVER")

        

        

    
        
        
