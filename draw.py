# define a lotto draw class
import game_config
from drum import Drum


class Draw:

    _draw_number: int

    def __init__(self, draw_number):
        self._draw_number = draw_number
        self._done = False
        self._drum = Drum()
        self._balls_drawn = []
        
    def number(self):
        return self._draw_number


    def do_draw(self):
        if not self._done:
            for i in range(game_config.NUMBER_OF_BALLS_PER_DRAW):
                self._balls_drawn.append(self._drum.draw())
            self._done = True
        else:
            raise DrawAlreadyDoneException()


    def balls_drawn(self):
        if not self._done:
            self.do_draw()
        return self._balls_drawn


class DrawAlreadyDoneException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)