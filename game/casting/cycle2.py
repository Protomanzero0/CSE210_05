import constants
from game.casting.snake import Snake
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color

class Cycle2(Snake):

    def __init__(self, head_color, tail_color):
        super().__init__(head_color, tail_color)
        self._segments = []
        self._prepare_body()

    def _prepare_body(self):
        x = int(constants.MAX_X * 3/4)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._head_color)
            self._segments.append(segment)


        