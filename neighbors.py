from global_variables import *

# Calculates a cell's neighbors (cells it touches)    
def _findNeighbors(cell, grid):
    # set each adjacent cell to NULL
    cell.update({"top_cell" : None})
    cell.update({"bottom_cell" : None})
    cell.update({"right_cell" : None})
    cell.update({"left_cell" : None})

    # if the adjacent cell is in bounds (i.e. the current cell is not an edge), update adjacent cells
    if (cell.get("y") < GRID_HEIGHT-1):
        cell.update({"top_cell" : grid[cell.get("x")][cell.get("y")+1]})
    if (cell.get("y") > 0):
        cell.update({"bottom_cell" : grid[cell.get("x")][cell.get("y")-1]})
    if (cell.get("x") < GRID_WIDTH-1):
        cell.update({"right_cell" : grid[cell.get("x")+1][cell.get("y")]})
    if (cell.get("x") > 0):
        cell.update({"left_cell" : grid[cell.get("x")-1][cell.get("y")]})
