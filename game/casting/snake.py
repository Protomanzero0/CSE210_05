import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, head_color, tail_color):
        super().__init__()
        self._segments = []
        self._head_color = head_color
        self._tail_color = tail_color
        self._prepare_body()


    def get_segments(self):
        return self._segments

    def move_next(self):
        self.grow_tail(1)
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]
    
    def turn_white(self):
        self._head_color = Color(255,255,255)
        self._tail_color = Color(255,255,255)

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._tail_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        pass