from line import Line
import game_config


# define the Ticket class
class Ticket:

    # constructor
    def __init__(self, lines_per_ticket=game_config.BALLS_DRAWN):
        self._lines_per_ticket = lines_per_ticket

        self._lines = []
        for i in range(self._lines_per_ticket):
            self._lines.append(Line())

    def num_lines(self):
        return self._lines_per_ticket

    def lines(self):
        return self._lines
