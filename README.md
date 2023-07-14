# Depth-First Search Maze-Generation
This Program uses a modified version of recursive depth-first search to traverse a grid and generate a maze. The grid is scalable and customizable. This Program uses the [Zelle Graphics Library](https://www.cs.swarthmore.edu/~adanner/cs21/s15/Labs/graphics.php) to visualize the maze.

There are multiple implementations for this design, but this program uses a recursive method: 

1. Given a current cell as an input
2. Mark the current cell as visited
3. If the current cell has any in-bounds and unvisited neighbor cells:
    1. Randomly choose one of the unvisited neighbors
    2. Remove the wall between the current cell and the chosen cell
    3. Call the function recursively with the chosen cell as the input
       

Example maze:

![Sceen Shot](https://github.com/Rhys-sg/Maze-Generation/assets/127057159/257d6ed9-77e5-464d-8c77-c5250854cf3b)
