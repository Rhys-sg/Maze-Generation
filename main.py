import algorithm
import grid_constructor
import graphics

from global_variables import *

def main():
    window = graphics.GraphWin("Screen", WINDOW_WIDTH, WINDOW_HEIGHT)

    grid = grid_constructor.grid(window)

    algorythm.findPath(grid[0][0], grid)

    # pause for click in window, then closes
    window.getMouse()
    window.close()
    
main()
