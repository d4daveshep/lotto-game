# this is a main test file

from drum import Drum
from line import Line

SIZE = 10
drum = Drum(SIZE)
drawn_balls = []
for i in range(SIZE):
    drawn_balls.append(drum.draw())
    
print(drawn_balls)

line = Line(6,40)
print(line.numbers())


    


