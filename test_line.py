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
    assert line.get_numbers() == sorted(line.get_numbers())

def test_manually_chosen_line(new_line):
    line = new_line

    from line import LineException

    my_numbers = [6,5,4,3,2,1]

    line.pick_numbers(my_numbers)

    # check numbers are stored in ascending order
    assert line.get_numbers() == sorted(my_numbers)

    # check correct line number count
    my_numbers = [1,2,3,4,5] # too few
    with pytest.raises(LineException, message="Expecting LineException"):
        line.pick_numbers(my_numbers)

    my_numbers = [1,2,3,4,5,6,7] # too many
    with pytest.raises(LineException, message="Expecting LineException"):
        line.pick_numbers(my_numbers)

    # check we can't add numbers that aren't valid balls in the drum
    my_numbers = [0,1,2,3,4,5]
    with pytest.raises(LineException, message="Expecting LineException"):
        line.pick_numbers(my_numbers)



