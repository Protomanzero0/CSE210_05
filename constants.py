from game.shared.color import Color
from game.shared.point import Point

COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Snake"
SNAKE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
LEFT= Point(-CELL_SIZE, 0)
RIGHT= Point(CELL_SIZE, 0)
UP= Point(0, -CELL_SIZE)
DOWN= Point(0, CELL_SIZE)
