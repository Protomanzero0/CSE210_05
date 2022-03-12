import constants
from game.scripting.action import Action

class ControlPlayerOne(Action): 

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._direction = constants.RIGHT

    def execute(self, cast, script):
          # left
        if self._keyboard_service.is_key_down('a') and self._direction != constants.RIGHT:
            self._direction = constants.LEFT
        
        # right
        if self._keyboard_service.is_key_down('d') and self._direction != constants.LEFT:
            self._direction = constants.RIGHT
        
        # up
        if self._keyboard_service.is_key_down('w') and self._direction != constants.DOWN:
            self._direction = constants.UP
        
        # down
        if self._keyboard_service.is_key_down('s') and self._direction != constants.UP:
            self._direction = constants.DOWN
        
        cycle1 = cast.get_first_actor("snakes")
        cycle1.turn_head(self._direction)