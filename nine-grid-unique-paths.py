from math import factorial

def grid_unique_paths(A,B):
    A -= 1
    B -= 1
    return factorial(A+B) // (factorial(A) * factorial(B))


print(grid_unique_paths(3,3))
