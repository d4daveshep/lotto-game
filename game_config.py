# specify the game parameters
import random

NUMBER_OF_BALLS_IN_DRUM = 40
NUMBER_OF_BALLS_PER_DRAW = 6
NUMBER_OF_BONUS_BALLS_PER_DRAW = 1
DEFAULT_LINES_PER_TICKET = 10

# use this for testing purposes to predict the sequence
random.seed(0)

# define the winning divisions
DIVISION = {
    (6,0): '1st division',
    (5,1): '2nd division',
    (5,0): '3rd division',
    (4,1): '4th division',
    (4,0): '5th division',
    (3,1): '6th division',
    (3,0): 'Bonus ticket'
}
