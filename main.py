# this is a main test file

from drum import Drum
from line import Line
from ticket import Ticket
from draw import Draw

# create a new draw
draw = Draw(1)
draw.print_draw()

# create a ticket for the draw
ticket = Ticket()
ticket.print_ticket()

# do the draw
draw.do_draw()
draw.print_draw()

# check the ticket
for line in ticket.lines():
    win = draw.check_ticket_line(line)
    line.print_line()
    print('Won',win)

# lines = ticket.lines()
# print()
# print(lines[0].print_line())
