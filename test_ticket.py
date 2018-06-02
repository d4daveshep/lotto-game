import pytest

LINES = 6

@pytest.fixture
def new_ticket():
    from ticket import Ticket
    return Ticket(LINES)

def test_create_ticket(new_ticket):
    ticket = new_ticket
    
    # right number of lines?
    assert ticket.num_lines() == LINES
    
    