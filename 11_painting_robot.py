from computer import Computer
from enum import Enum
from collections import defaultdict

class Orientation(Enum):
    LEFT = 0 
    RIGHT = 1
    UP = 2
    DOWN = 3

orientation = Orientation.UP
x = 0
y = 0
colors = defaultdict(int)
painted = set()

with open("11_input.txt") as _file:
    program = [int(num) for num in _file.read().split(",")]

computer = Computer(program)
current_location = (x, y)
colors[(x,y)] = 1

while(not computer.done):
    current_color = colors[(x,y)]
    new_color, turn_right = computer.calculate([current_color])
    colors[(x,y)] = new_color
    painted.add((x,y))
    computer.clear_output()

    if orientation == Orientation.UP:
        if turn_right:
            orientation = Orientation.RIGHT
            x+=1
        else:
            orientation = Orientation.LEFT
            x-=1

    elif orientation == Orientation.DOWN:
        if turn_right:
            orientation = Orientation.LEFT
            x-=1    
        else:
            orientation = Orientation.RIGHT
            x+=1

    elif orientation == Orientation.LEFT:
        if turn_right:
            orientation = Orientation.UP
            y-=1    
        else:
            orientation = Orientation.DOWN
            y+=1

    elif orientation == Orientation.RIGHT:
        if turn_right:
            orientation = Orientation.DOWN
            y+=1    
        else:
            orientation = Orientation.UP
            y-=1

print(len(colors))
print("Painted:", len(painted))
print("White painted:", sum(colors.values()))

x_keys, y_keys = list(zip(*colors.keys()))
x_max = max(x_keys) + 1
y_max = max(y_keys) + 1
print(x_max, y_max)

# Print the identification image
import numpy as np
array = np.zeros((y_max, x_max))
for x in range(x_max):
    for y in range(y_max):
        array[y, x] = colors[(x,y)]

print(array[:,:20])
print(array[:,20:])

# Print using string
tapestry = "\n".join(["".join([str(colors[(x,y)]) for x in range(x_max)]) for y in range(y_max)])
tapestry = tapestry.replace("0", " ").replace("1", "X")
print(tapestry)
