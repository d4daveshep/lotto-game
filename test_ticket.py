import pytest

LINES_ON_TICKET = 6


@pytest.fixture
def new_ticket():
    from ticket import Ticket
    return Ticket(LINES_ON_TICKET)


def test_create_ticket(new_ticket):
    ticket = new_ticket

    # right number of lines?
    assert ticket.num_lines() == LINES_ON_TICKET
