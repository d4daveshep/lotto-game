from line import Line
import game_config


# define the Ticket class
class Ticket:

    # constructor
    def __init__(self, lines_per_ticket=game_config.DEFAULT_LINES_PER_TICKET):
        self._lines_per_ticket = lines_per_ticket

        self._lines = []
        for i in range(self._lines_per_ticket):
            self._lines.append(Line())

    def num_lines(self):
        return self._lines_per_ticket

    def lines(self):
        return self._lines

    def print_ticket(self):
        print('Ticket')
        print('-' * 6)
        for num, line in enumerate(self._lines,1):
            print('Line',num,':',line.get_numbers())
        print()


