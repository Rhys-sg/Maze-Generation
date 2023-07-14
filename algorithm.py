import numpy
from global_variables import *

# global set used to store visited cell [x,y], use set for O(1) lookup
visited = set()

# Create "start" and "end" of the maze
#   randomly generates the start side
#   calculates the opposite side of the grid
#   erases the "entrance" and "exits"
#   then calls recursive function, so long as the start is valid
def findPath(cell, grid):
  start_side_order = [("top", "bottom"), ("bottom", "top"), ("left", "right"), ("right", "left")] # ordered pair for "start" and "end" of maze
  numpy.random.shuffle(start_side_order)
  for side in start_side_order:
    if (cell.get(side[0] + "_cell") == None):
      cell.get(side[0] + "_line").undraw()
      grid[len(grid[0]) - cell.get("x") - 1][len(grid) - cell.get("y") - 1].get(side[1] + "_line").undraw() # calculate corresponding "end" point/side

      _findPath(cell) # start recursion
      return
    
  print("Invalid start given")


# Recursive Depth-First Search-based algorithm 
def _findPath(cell):
  # current cell is added to set
  visited.add((cell.get("x"), cell.get("y")))

  # randomize what way to go next--shuffles array to store what the algorithm needs to try later
  successors = ["top", "bottom", "left", "right"]
  numpy.random.shuffle(successors)

  # Try each direction generated above. If an option is valid, erase the line between and call recursion
  for next in successors:
    if _isInvalid(cell.get(next + "_cell")):
      continue
    cell.get(next + "_line").undraw() 
    _findPath(cell.get(next + "_cell"))


# Helper function used to more efficiently tell if a cell is in bounds, and not yet visited
def _isInvalid(cell):
  return ((cell == None) or ((cell.get("x"), cell.get("y")) in visited))
