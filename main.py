import os
import sys

src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
sys.path.append(src_path)

from grid import grid, iswithinbounds
from pathfinder import bfs

rows = int(input("\nEnter the number of rows in the table: "))
columns = int(input("Enter the number of columns in the table: "))

FOUR_DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
EIGHT_DIRECTIONS = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

dir_req = input("Do you want 4 or 8 directional movement (4/8): ") #Request the user for directional movement to be used
if dir_req == '4':
    directions = FOUR_DIRECTIONS
elif dir_req == '8':
    directions = EIGHT_DIRECTIONS
else:
    print("Please type either 4 or 8")
    sys.exit()

grid(rows, columns)

start_row = int(input("\nEnter the starting row: "))
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

path = bfs(start, end, rows, columns, directions)

print(path)