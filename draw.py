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
        self._bonus_balls_drawn = []

    def number(self):
        return self._draw_number

    def do_draw(self):
        if not self._done:
            for i in range(game_config.NUMBER_OF_BALLS_PER_DRAW):
                self._balls_drawn.append(self._drum.draw())
            for i in range(game_config.NUMBER_OF_BONUS_BALLS_PER_DRAW):
                self._bonus_balls_drawn.append(self._drum.draw())
            self._done = True
        else:
            raise DrawAlreadyDoneException()

    def print_draw(self):
        print('Draw')
        print('-' * 4)
        if not self._done:
            print('Ready to draw',game_config.NUMBER_OF_BALLS_PER_DRAW,'balls and',game_config.NUMBER_OF_BONUS_BALLS_PER_DRAW,'bonus ball')
        else:
            print('Drawn',len(self._balls_drawn),'balls and ',len(self._bonus_balls_drawn),'bonus ball')
            print('Balls drawn are', sorted(self._balls_drawn), 'and bonus ball', self._bonus_balls_drawn)
        print()

    def balls_drawn(self):
        if not self._done:
            self.do_draw()
        return self._balls_drawn

    def bonus_balls_drawn(self):
        if not self._done:
            self.do_draw()
        return self._bonus_balls_drawn

    def check_ticket_line(self, line):
        if not self._done:
            raise DrawNotDoneException()

        # count the number of balls that match
        matches = 0
        bonus_matches = 0

        for ball in line.get_numbers():
            if ball in self._balls_drawn:
                matches = matches + 1
            if ball in self._bonus_balls_drawn:
                bonus_matches = bonus_matches + 1

        win = (matches,bonus_matches)   # tuple of matching balls and bonus ball

        # look up which division we won (or not)
        if win not in game_config.DIVISION.keys():
            return None
        else:
            return game_config.DIVISION[win]



class DrawAlreadyDoneException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)

class DrawNotDoneException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
