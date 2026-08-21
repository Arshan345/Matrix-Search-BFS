from collections import deque
from grid import iswithinbounds, getneighbours

def reconstructpath(came_from, start, end):
    path = [end]
    current_cell = end
    while current_cell != start:
        current_cell = came_from[current_cell]
        path.append(current_cell)
    path.reverse()
    return path
        

def bfs(start, end, rows, columns):
    queue = deque([start])
    visited = {start}
    came_from = {}
    while queue:
        current = queue.popleft()
        if current == end:
            return reconstructpath(came_from, start, end)
        val_cand = getneighbours(current, rows, columns)
        for i in val_cand:
            if i in visited:
                pass
            else:
                visited.add(i)
                queue.append(i)
                came_from[i] = current
    return None
