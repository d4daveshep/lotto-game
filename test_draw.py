import pytest
import game_config


@pytest.fixture
def new_draw():
    from draw import Draw
    return Draw(1)

@pytest.fixture
def new_ticket():
    from ticket import Ticket
    return Ticket()


def test_thedraw(new_draw):
    draw = new_draw

    # do the draw
    draw.do_draw()

    # check we get an exception if we try to do another draw
    from draw import DrawAlreadyDoneException
    with pytest.raises(DrawAlreadyDoneException, message="Expecting DrawAlreadyDoneException"):
        draw.do_draw()

    # check we draw out the correct number of balls
    assert game_config.NUMBER_OF_BALLS_PER_DRAW == len(draw.balls_drawn())
    assert game_config.NUMBER_OF_BONUS_BALLS_PER_DRAW == len(draw.bonus_balls_drawn())


def test_check_ticket(new_draw, new_ticket):
    pass
    # draw = new_draw
    # # TODO we need to finish checking the ticket
    # matches = draw.check_ticket(new_ticket)
    #
    # print('line has', matches, 'matches')


def test_check_line_in_ticket(new_draw, new_ticket):
    draw = new_draw
    draw.do_draw()

    # OK let's cheat a bit

    # check 1st division winner
    from line import Line
    line = Line()
    line.pick_numbers(draw.balls_drawn())

    win = draw.check_ticket_line(line)
    assert win == game_config.DIVISION[(6,0)]

    # check 2nd division winner
    bonus_ball = draw.bonus_balls_drawn()[0]
    numbers = line.get_numbers()
    if bonus_ball in numbers:
        assert False
    numbers[0] = bonus_ball
    line.pick_numbers(numbers)
    win = draw.check_ticket_line(line)
    assert win == game_config.DIVISION[(5, 1)]

    # check 3rd division winner by replacing a winning number with 1
    if 1 in numbers:
        assert False
    numbers[0] = 1
    line.pick_numbers(numbers)
    win = draw.check_ticket_line(line)
    assert win == game_config.DIVISION[(5, 0)]

    # check 4th division winner
    numbers = line.get_numbers()
    if bonus_ball in numbers:
        assert False
    numbers[1] = bonus_ball
    line.pick_numbers(numbers)
    win = draw.check_ticket_line(line)
    assert win == game_config.DIVISION[(4, 1)]

    # check 5th division winner by replacing another winning number with 2
    numbers = line.get_numbers()
    if 2 in numbers:
        assert False
    numbers[1] = 2
    line.pick_numbers(numbers)
    win = draw.check_ticket_line(line)
    assert win == game_config.DIVISION[(4, 0)]
    # print(line.print_line())

    # check 6th division winner
    numbers = line.get_numbers()
    if bonus_ball in numbers:
        assert False
    numbers[2] = bonus_ball
    line.pick_numbers(numbers)
    win = draw.check_ticket_line(line)
    assert win == game_config.DIVISION[(3, 1)]

