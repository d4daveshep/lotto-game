from drum import Drum
import game_config


# define the Line class representing a line of numbers on a ticket

class Line:

    # constructor
    def __init__(self, numbers_per_line=game_config.NUMBER_OF_BALLS_PER_DRAW,
                 balls_in_drum=game_config.NUMBER_OF_BALLS_IN_DRUM):
        self._numbers_per_line = numbers_per_line
        self._balls_in_drum = balls_in_drum

        self._numbers = []

        # set up temporary Drum to pick our line numbers from
        drum = Drum(balls_in_drum)
        for i in range(numbers_per_line):
            self._numbers.append(drum.draw())
        self._numbers = sorted(self._numbers)

    def numbers_per_line(self):
        return self._numbers_per_line

    def pick_numbers(self, chosen_numbers):
        if self._numbers_per_line != len(chosen_numbers):
            raise LineException("Line must have",self._numbers_per_line,"numbers per line")
        else:
            self._numbers = sorted(chosen_numbers)

        # TODO raise exception if any chosen number isn't actually a valid ball in the drum


    def get_numbers(self):
        return self._numbers

    def print_line(self):
        print(self._numbers)

class LineException(Exception):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)