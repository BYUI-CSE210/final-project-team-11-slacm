import constants
from game.casting.actor import Actor

class Car(Actor):
    """
    An enemy to the frog.
    
    The responsibility of Car is to move horizontally across the screen.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self.set_text("C")
        self.set_font_size(constants.CAR_CELL_SIZE)