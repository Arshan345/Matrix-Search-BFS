import os
import sys

src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
sys.path.append(src_path)

from grid import grid, iswithinbounds, getneighbours
from pathfinder import reconstructpath, bfs

rows = 8
columns = 8

grid(rows, columns)

start_row = int(input("Enter the starting row: "))
start_col  = int(input("Enter the starting column: "))
end_row = int(input("Enter the ending row: "))
end_column = int(input("Enter the ending column: "))

start = (start_row, start_col)
end = (end_row,end_column)
if not iswithinbounds(start,rows,columns):
    print("Error! The starting cell must be within the given matrix")
    quit() 
elif not iswithinbounds(end,rows,columns):
    print("Error! The ending cell must be within the given matrix")
    quit()

path = bfs(start, end, rows, columns)

print(path)