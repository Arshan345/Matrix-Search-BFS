def grid(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        print("")
        for j in range(columns):
            cell = (i, j)
            row.append(cell)
            print(cell, end="  ")
        matrix.append(row)
    return matrix

def iswithinbounds(cell, rows, columns):
    rowcheck, columncheck = cell
    if rowcheck < 0 or rowcheck > rows-1:
        return False
    elif columncheck < 0 or columncheck > columns-1:
        return False
    else:
        return True
rows = 8
columns = 8

cell_check = iswithinbounds((5,9), rows, columns)


def iswalkable():
    pass
def getneighbours(cell, rows, columns):
    par_row, par_col = cell #Parent rows and cols from which the 4 candidates are derived
    candidates = [(par_row-1,par_col),(par_row+1,par_col),(par_row,par_col-1),(par_row,par_col+1)] #creates a list of possible cells in 4 directions i.e. up,down,left,right
    val_cand = [] # List of the valid candidates
    for i in candidates:
        if iswithinbounds(i,rows,columns):
            val_cand.append(i)
    return val_cand
    



def mark_unwalkable():
    pass