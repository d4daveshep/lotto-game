import random
import game_config


# define the Drum class
class Drum:

    # constructor
    def __init__(self, size=game_config.NUMBER_OF_BALLS_PER_DRAW):
        self.size = size

        # list of balls left in the drum
        self.balls = [x + 1 for x in range(self.size)]

        # Return the number of balls left in the drum

    def num_balls(self):
        return len(self.balls)

    # check a ball is in the drum?
    def has_ball(self, ball):
        return ball in self.balls

    # draw a random ball out of the drum
    def draw(self):
        if self.num_balls() < 1:
            raise EmptyDrumException("Drum is empty")
        ball_num = random.randint(0, len(self.balls) - 1)
        ball = self.balls.pop(ball_num)
        return ball


# define the EmptyDrumException
class EmptyDrumException(RuntimeError):
    pass
