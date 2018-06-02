import pytest

NUMBERS_PER_LINE = 6
BALLS_IN_DRUM = 40


@pytest.fixture
def new_line():
    from line import Line
    return Line(NUMBERS_PER_LINE, BALLS_IN_DRUM)


def test_create_line(new_line):
    line = new_line

    # right numbers?
    assert line.numbers_per_line() == NUMBERS_PER_LINE

    # check numbers are in ascending order
    assert line.numbers() == sorted(line.numbers())
