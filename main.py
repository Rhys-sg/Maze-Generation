import DFS
import create_dict_cell_walls
import graphics


grid_width = 30
grid_height = 30
grid_cell_side_length = 10
grid = [[{"pos" : (x, y)} for y in range(grid_height)] for x in range(grid_width)]

boarder_width = grid_cell_side_length * grid_width
boarder_height = grid_cell_side_length * grid_height
window_width = 720
window_height = 540

window = graphics.GraphWin("Screen", window_width, window_height)

def main():
    create_dict_cell_walls.create_dict_cell_walls(grid, window, window_width, window_height, boarder_width, boarder_height, grid_cell_side_length)

    # pause for click in window, then closes
    window.getMouse()
    window.close()
    
main()