# Matrix Search — BFS Pathfinder on an 8x8 Grid

A simple, function-based Python program that finds the shortest path between two points on an 8x8 grid using Breadth-First Search (BFS).

## Overview

The program works on a matrix, with each element called a cell. The program is given a starting cell and an ending cell. It finds the shortest path on an unweighted grid between the two points using Breadth-First Search (BFS).
The specific property of Breadth-First Search (BFS) that guarantees shortest-path correctness on an unweighted grid is its level-by-level exploration. BFS systematically explores all nodes at the current depth level before moving to the next depth level, ensuring that the first node visited is the one with the shortest distance from the source node. This property is crucial because it allows BFS to maintain the order of nodes based on their distance, which is essential for finding the shortest path in unweighted graphs.


## Features

- [ ] 8x8 grid represented as `(row, col)` coordinates
- [ ] Shortest-path search via BFS, 4-directional movement (up/down/left/right)
- [ ] User-provided start and end points


## How It Works

The grid is represented by a matrix. Every 'cell' is made up of a tuple with its respective row and column. The program uses Breadth-First Search--it checks every cell and its neighbours using the `deque()` function in python. This allows to efficiently add and remove elements from the queue during the cell checking procedure.
The program is given a starting cell by the user, it adds this cell to the queue then marks it as visited then removes the initial cell from the queue. Then it extrapolates the possible neighbour cells in the four cardinal directions, and adds the valid cells into the queue, while marking these cells as visited. This process repeats until the loop reaches the end cell. 
Each cell is stored in a `visited` set and each cell is stored along with its parent cell as key/value pair in the `came_from` dictionary.
At the end of the loop, the program traces back from the end cell to the parent cell using this dictionary and adding each element into an array called `path`. Now since this array is end to start, a simple `.reverse()` function reverses the order, then the array is printed as output.


## Project Structure

```
matrix-search/
├── README.md
├── .gitignore
├── main.py
└── src/
    ├── grid.py         # grid creation, bounds-checking, neighbor lookup
    └── pathfinder.py   # BFS search and path reconstruction
```

## Requirements

Python 3.13.1
All packages used are included with the base install of python

## Installation

```bash
git clone https://github.com/Arshan345/Matrix-Search-BFS.git
cd matrix-search
```

## Usage

```bash
python main.py
```
The program will initially print an 8x8 grid.From this grid, the program asks the user for four separate inputs:
the starting and ending row num
the starting and ending column num

Afterwards the program prints out an array of the path from the start to the end.
## Roadmap / Future Improvements

- [ ] Support obstacles (unwalkable cells)
- [ ] Visualize the path drawn on the grid (not just a list of coordinates)
- [ ] Unit tests (`tests/`)
- [ ] Support weighted grids.
- [ ] Add omni-directional (8 direction) movement

## License

