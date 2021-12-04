from math import factorial

def grid_unique_paths(A,B):
    grid = []

    for _ in range(A):
        grid.append([0]*B)
    for j in range(B):
        grid[A-1][j] = 1

    for i in range(A):
        grid[i][B-1] = 1
    for i in range(A-2,-1,-1):
        for j in range(B-2, -1, -1):
            grid[i][j] = grid[i][j+1] + grid[i+1][j]

    return grid[0][0]


print(grid_unique_paths(7,3))
