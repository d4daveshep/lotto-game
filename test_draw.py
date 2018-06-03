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


def test_check_ticket():
    pass
#    assert 0

def test_check_line_in_ticket(new_draw, new_ticket):
    draw = new_draw
    draw.do_draw()

    ticket = new_ticket
    line = ticket.lines()[0]
    print(line.print_line())


