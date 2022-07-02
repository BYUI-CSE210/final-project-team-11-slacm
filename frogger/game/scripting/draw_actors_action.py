from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        coin = cast.get_first_actor("coins")
        obstacle = cast.get_first_actor("obstacles")
        frog = cast.get_first_actor("frog")


        self._video_service.clear_buffer()
        self._video_service.draw_actor(coin)
        self._video_service.draw_actor(score)
        self._video_service.draw_frog(frog)
        self._video_service.draw_obstacle(obstacle)
        self._video_service.flush_buffer()