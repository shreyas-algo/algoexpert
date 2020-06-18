def spiralTraverse(array):
    arr_len = len(array)
    # init
    direction = "right"
    row, col = 0, 0
    # boundaries
    top_boundary = 0
    left_boundary = 0
    right_boundary = len(array[0])	# assumed symmetric arrays and at least one row
    bottom_boundary = len(array)
    # result mapping
    spiral = []
    spiral.append(array[row][col])
    spiral_length = 1
    while spiral_length < arr_len:
        row, col = getNextPoint(direction, row, col)
        if direction == "right" and exceedingRight(row, col):
            row, col = pivotDown(direction, right_boundary)
            
        if direction == "down" and exceedingDown(row, col):
            row, col = pivotLeft(direction, bottom_boundary)
            
        if direction == "left" and exceedingLeft(row, col):
            row, col = pivotTop(direction, left_boundary)
        
        if direction == "top" and exceedingTop(row, col):
            row, col = pivotRight(direction, top_boundary)
        
        # technically not required as length check used in while
        if (row, col) == (-1, -1):
            break
        spiral_length += 1
    return spiral
