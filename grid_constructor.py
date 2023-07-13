import points
import neighbors
import lines

from global_variables import *

# Grid Constructor: Creates grid based on global variables
#   Calculates the points and lines necessary to make a rectangle for each cell in the grid
#   Updates shared lines in order (two touching lines share a wall)
#   We use lines instead of rectangles so that we can remove individual "walls."
#   Adds all calculated values (including a cell's regional center (x,y) coordinates) to dict
#   Returns grid
def grid(window):
    grid = [[{"x" : x, "y" : y} for y in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)]

    # for every cell:
    for row in grid:
        for cell in row:
            x = cell.get("x")
            y = cell.get("y")
            
            # Unpack elements of return from _calculatePoints as parameters for _calculateLines
            lines._calculateLines(cell, x, y, window, grid, *points._calculatePoints(cell, x, y))
            neighbors._findNeighbors(cell, grid)

    return grid
