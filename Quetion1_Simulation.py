
from random import random
import copy

def print_grid(grid):
    print("Grid:")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end = " ")
        print()

p = 0.6
grid_size = 3 

number_of_runs = 100000
averege_game_length = 0

for n in range(number_of_runs):
    grid = [[0 for j in range(grid_size)] for i in range(grid_size)]

    # inital point (1, 1)
    grid[1][1] = 1
    current_point = [1,1] # i,j
    moves = 0

    # print(f"move: {move}")
    # print_grid(grid)
    # print(f"current_point: {current_point}")

    while (True):
        new_point = copy.deepcopy(current_point)
        if random() < p: # horizontally
            if random() < 0.5: # up
                if not current_point[0] == 0:
                    new_point[0] -= 1
                else:
                    new_point[0] += 1
            else:  # down
                if not current_point[0] == len(grid) - 1:
                    new_point[0] += 1
                else:
                    new_point[0] -= 1
        else: # vertically
            if random() < 0.5: # left
                if not current_point[1] == 0:
                    new_point[1] -= 1
                else:
                    new_point[1] += 1
            else:  # right
                if not current_point[1] == len(grid[0]) - 1:
                    new_point[1] += 1
                else:
                    new_point[1] -= 1
        
        grid[current_point[0]][current_point[1]] = 0
        grid[new_point[0]][new_point[1]] = 1

        current_point = copy.deepcopy(new_point)

        moves += 1

        # print(f"move: {move}")
        # print_grid(grid)
        # print(f"current_point: {current_point}")

        if current_point == [0,0] or current_point == [0,2] or current_point == [2,0] or current_point == [2,2]: # End
            averege_game_length += moves/number_of_runs
            break

print(f"p={p}")
print(f"Average game length: {averege_game_length}")

