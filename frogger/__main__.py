from game.casting.cast import Cast
from game.casting.coin import Coin
from game.casting.score import Score
from game.casting.frog import Frog
from game.casting.lives import Lives
from game.casting.difficulty import Difficulty
from game.scripting.script import Script
from game.scripting.control_frog_action import ControlFrogAction
from game.scripting.create_car_action import CreateCarAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("coins", Coin())
    cast.add_actor("frogs", Frog())
    cast.add_actor("scores", Score())
    cast.add_actor("lives", Lives())
   
    # start the game
    difficulty = Difficulty()
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlFrogAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(difficulty))
    script.add_action("update", CreateCarAction(difficulty))
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
