import graphics
from global_variables import *

# Calculates the four corner points and center point
def _calculatePoints(cell, x, y):
    # calculate regional (x,y) coordinates for the bottom left
    bottom_left_regional_x = (WINDOW_WIDTH / 2) - (BOARDER_WIDTH / 2) + (GRID_CELL_SIDE_LENGTH * x)
    bottom_left_regional_y = (WINDOW_HEIGHT / 2) + (BOARDER_HEIGHT / 2) - (GRID_CELL_SIDE_LENGTH * y)

    # add center and bottom left regional (x,y) coordinates to dict
    cell.update({"regional_top_left" : [bottom_left_regional_x, bottom_left_regional_y]})

    # add / subtract size of grid from bottom left regional (x,y) coordinates to get each point of rectangle
    bottom_left_pt = graphics.Point(bottom_left_regional_x, bottom_left_regional_y)
    bottom_right_pt = graphics.Point(bottom_left_regional_x + GRID_CELL_SIDE_LENGTH, bottom_left_regional_y)
    top_left_pt = graphics.Point(bottom_left_regional_x, bottom_left_regional_y - GRID_CELL_SIDE_LENGTH)
    top_right_pt = graphics.Point(bottom_left_regional_x + GRID_CELL_SIDE_LENGTH, bottom_left_regional_y - GRID_CELL_SIDE_LENGTH)

    return bottom_left_pt, bottom_right_pt, top_left_pt, top_right_pt