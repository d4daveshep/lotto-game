# unit tests for Drum class
# from drum import Drum

import pytest

SIZE = 10


# fixture to create a new drum for each test
@pytest.fixture
def new_drum():
    from drum import Drum
    return Drum(SIZE)


# test the drum is created with correct number of balls
def test_create_drum(new_drum):
    drum = new_drum

    # right num of balls?
    assert drum.num_balls() == SIZE

    # contains one of each ball
    for b in range(1, SIZE + 1):
        assert drum.has_ball(b)


# test drawing a ball removes it from the drum
def test_draw_ball(new_drum):
    drum = new_drum
    ball = drum.draw()
    assert drum.has_ball(ball) == False


# test we can draw all the balls out
def test_draw_all_balls(new_drum):
    drum = new_drum

    # draw out all balls
    drawn_balls = []
    for i in range(SIZE):
        drawn_balls.append(drum.draw())

    # check num left in drum
    assert drum.num_balls() == 0

    # check we got the right number from the drum
    assert len(drawn_balls) == SIZE

    # check we've got one of each ball
    for b in range(1, SIZE + 1):
        assert b in drawn_balls

    # get an Error if we try to get a ball from an empty drum
    from drum import EmptyDrumException
    with pytest.raises(EmptyDrumException):
        drum.draw()
