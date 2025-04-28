import cellpylib as cpl

import cellpylib3d

import numpy as np
# empty 3d grid
grid = cellpylib3d.init_simple3d(15, 15, 15, val=0) # init empty 3d grid

# oscilating shape from donut
grid[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1
#grid[:, [1], 4, [4, 5, 6, 6]] = 1

# run using GOL ruleset for N timesteps
cellular_automaton = cellpylib3d.evolve3d(grid, timesteps=100, neighbourhood='Moore', apply_rule=cellpylib3d.game_of_life_rule_3d)

# animate
cellpylib3d.plot3d_animate(cellular_automaton, title='3D Game of Life',face_color='black', edge_color='red', save=True, interval=750)

cells = np.array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[11,12,13],[14,15,16],[17,18,19]],
    [[21,22,23],[24,25,26],[27,28,29]]], 
    dtype=int)

print(cells[0,1,2])
print(cells[2,1,0])
print(cells[0,2,1])