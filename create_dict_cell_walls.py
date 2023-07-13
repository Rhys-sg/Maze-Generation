import graphics

# Calculates the points and lines necissary to make a rectangle for each cell in the grid
#   We use lines instead of rectangles so that we can remove individual "walls"
#   Adds all calculated values (including a cell's regional center (x,y) coordinates) to dict
#   No return
def create_dict_cell_walls(grid, window, window_width, window_height, boarder_width, boarder_height, grid_cell_side_length):
    for row in grid:
        for column in row:
            # calculate regional (x,y) coordinates for the top left of every point
            xy = column.get("pos")
            top_left_regional_xy = [(window_width / 2) - (boarder_width / 2) + (grid_cell_side_length * xy[0]), (window_height / 2) + (boarder_height / 2) - (grid_cell_side_length * xy[1])]

            # add center and top left regional (x,y) coordinates to dict for easy access
            column.update({"regional_top_left" : top_left_regional_xy})
            column.update({"regional_center" : [top_left_regional_xy[0] + (grid_cell_side_length / 2), top_left_regional_xy[1] - (grid_cell_side_length / 2)]})
            
            # add / subtract size of grid from top left regional (x,y) coordinates to get each point of rectangle
            top_left_pt = graphics.Point(top_left_regional_xy[0], top_left_regional_xy[1])
            top_right_pt = graphics.Point(top_left_regional_xy[0] + grid_cell_side_length, top_left_regional_xy[1])
            bottom_left_pt = graphics.Point(top_left_regional_xy[0], top_left_regional_xy[1] - grid_cell_side_length)
            bottom_right_pt = graphics.Point(top_left_regional_xy[0] + grid_cell_side_length, top_left_regional_xy[1] - grid_cell_side_length)

            # calculate lines of rectangle and add to dict
            column.update({"top_line" : graphics.Line(top_left_pt, top_right_pt)})
            column.update({"right_line" : graphics.Line(top_right_pt, bottom_right_pt)})
            column.update({"bottom_line" : graphics.Line(bottom_left_pt, bottom_right_pt)})
            column.update({"left_line" : graphics.Line(top_left_pt, bottom_left_pt)})
            
            # draw each line to form rectangle
            column.get("top_line").draw(window)
            column.get("right_line").draw(window)
            column.get("bottom_line").draw(window)
            column.get("left_line").draw(window)