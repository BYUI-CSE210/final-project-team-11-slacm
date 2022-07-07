from game.shared.color import Color


COLUMNS = 60
ROWS = 40
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)

CAPTION = 'Frogger Clone'

#lives
LIFE_SPACING = 25
LIFE_POSITION_START = 20
LIFE_COUNT = 3

#data for car spawning
SPAWN_INTERVAL = 20 #decides how many frames in between each new car
DIFFICULTY_INTERVAL = 1
CAR_SIZE = 3 #this will require some playing with to implement properly