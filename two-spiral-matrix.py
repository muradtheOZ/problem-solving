def spiral_order(matrix):
    spiral_order = []
    if len(matrix) == 0:
        return spiral_order
    m = len(matrix)
    n = len(matrix[0])

    left,top = 0,0 
    right,bottom = n-1, m-1

    direction = 0

    while len(spiral_order) < m* n:
        if direction == 0:
            #left to right direction
            for i in range(left, right+1):
                spiral_order.append(matrix[top][i])
            top += 1
        #top to bottom direction
        elif direction == 1:
            for i in range(top, bottom+1):
                spiral_order.append(matrix[i][right])
            right -= 1

        #right to left direction
        elif direction == 2:
            for i in range(right, left-1, -1):
                spiral_order.append(matrix[bottom][i])
            bottom -= 1
        #bottom to top direction
        elif direction == 3:
            for i in range(bottom, top-1, -1):
                spiral_order.append(matrix[i][left])
            left += 1
        direction = (direction + 1) % 4
    return spiral_order
    """
    1 2 3
    4 5 6
    7 8 9
    """
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order(matrix))
