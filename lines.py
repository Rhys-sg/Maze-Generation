import graphics
from global_variables import *

# Calculates the lines between and surrounding cells  
def _calculateLines(cell, x, y, window, grid, bottom_left_pt, bottom_right_pt, top_left_pt, top_right_pt):
    # calculate or finds lines of rectangle and add to the cell's dict
    # if a cell is on the bottom row, create a lower line. Otherwise, use the shared line: lower line = the cell below's upper line
    if (y == 0):
        cell.update({"bottom_line" : graphics.Line(bottom_left_pt, bottom_right_pt)})
        cell.get("bottom_line").draw(window)
    else:
        cell.update({"bottom_line": grid[x][y-1].get("top_line")})

    # if a cell is on the left column, create a left line. Otherwise, use the shared line: left line = the cell to the left's right line
    if (x == 0):
        cell.update({"left_line" : graphics.Line(top_left_pt, bottom_left_pt)})
        cell.get("left_line").draw(window)
    else:
        cell.update({"left_line": grid[x-1][y].get("right_line")})

    # each cell makes its own right and top lines, and an undrawn rectangle in the center
    cell.update({"right_line" : graphics.Line(top_right_pt, bottom_right_pt)})
    cell.update({"top_line" : graphics.Line(top_left_pt, top_right_pt)})
    cell.get("right_line").draw(window)
    cell.get("top_line").draw(window)
