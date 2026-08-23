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

def iswalkable():
    pass
def getneighbours(cell, rows, columns,direction):
    par_row, par_col = cell #Parent rows and cols from which the 4 candidates are derived
    val_cand = [] # List of the valid candidates
    for i in direction:
        row_offset, col_offset = i
        candidate = ((par_row + row_offset), (par_col + col_offset))
        if iswithinbounds(candidate,rows,columns):
            val_cand.append(candidate)
    return val_cand
    



def mark_unwalkable():
    pass