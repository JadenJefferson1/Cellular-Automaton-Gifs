# Cellular Automata Overview
Cellular Automata (CA) are a grid of cells where each cell changes state base on a predefined set of rules. These rules dictate a cell's state based on the state of the cells neighbors and, or the cell itself. 

A cell can take on any state chosen by the creator. For example, we may have dead (black) cells and alive (white) cells. Alternatively, we might opt to use colors to represent different states such as as red, green, blue, yellow, etc. There are infinite possibilities to choose from. These cells make up a grid that can either be 1 dimensional, i.e, a linear string of cells, 2 dimensional which would be like a checkerboard and 3 dimensional like a cube. Each of these dimensions can take any random shape or size.

## Conway's Game of Life
The Game of life was devised by the British mathematician John Horton Conway. As a two-dimensional cellular automaton, each cell C, evaluates the state of its eight surrounding neighbors and calculates a sum \(N\), which is then used to determine its transition based on predefined rules for moving on to the next generation. Conway viewed these cells in a unique way and they can do interesting things such as die from loneliness or overcrowding, be born under the right conditions, or remain in their current state as dead or alive.

# Notes of Library Used
## cell2d.py
This uses numpy and matplotlib from the source. The cellular automata state is created and altered using a 2-dimensional numpy array. After each generation, this is array then saved and plotted in 2d graph using matplotlib. The plot of this graph is then stored as a single image. All images are then put into an array to create .gif file.

## cell3d.py
This is uses cellpylib3d, an extension of cellpylib that supports 3d modelling of cellular automata. The underlying workings of this library also uses numpy and matplotlib to make its animations. The library although is no longer maintained and requires python 3.6 to 3.7 with the official listed requirements being Python 3.6, numpy 1.15.4, and matplotlib 3.0.2. These are all older unmaintained versions with support for python 3.7 ending June 27th, 2023.

### Using cellpylib3d with recent versions of matplotlib
- In cellpylib3d/ca_functions3d.py
  - Delete line 129 ```ax.collections.clear()``` as ax.clear now properly handles the removal of collections and this line will cause errors.

### Creating rules
- In cellpylib3d/ca_rules.py
  - Insert your own function that returns the value of your cell.
- In cellpylib3d/__init\__.py
  - ```from .ca_rules import 'your_rule'```






