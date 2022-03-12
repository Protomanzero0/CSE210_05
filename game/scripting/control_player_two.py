import constants
from game.scripting.action import Action


class ControlPlayerTwo(Action): 

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._direction = constants.LEFT

    def execute(self, cast, script):
          # left
        if self._keyboard_service.is_key_down('j') and self._direction != constants.RIGHT:
            self._direction = constants.LEFT
        
        # right
        if self._keyboard_service.is_key_down('l') and self._direction != constants.LEFT:
            self._direction = constants.RIGHT
        
        # up
        if self._keyboard_service.is_key_down('i') and self._direction != constants.DOWN:
            self._direction = constants.UP
        
        # down
        if self._keyboard_service.is_key_down('k') and self._direction != constants.UP:
            self._direction = constants.DOWN
        
        cycle2 = cast.get_second_actor("snakes")
        cycle2.turn_head(self._direction)