def spiralTraverse(array):
    matrix_len = len(array) * len(array[0])
    # init
    direction = "right"
    row, col = 0, 0
    # boundaries
    top_boundary = 0
    left_boundary = -1
    right_boundary = len(array[0])	# assumed symmetric arrays and at least one row
    bottom_boundary = len(array)
    # result mapping
    spiral = []
    spiral.append(array[row][col])
    spiral_length = 1
    while spiral_length < matrix_len:
        
        row, col = getNextPoint(direction, row, col)
        # print(direction, row, col)
        if direction == "right" and exceedingRight(col, right_boundary):
            direction, right_boundary, row, col = pivotDown(row, col, direction, right_boundary, bottom_boundary)
            
        if direction == "down" and exceedingDown(row, bottom_boundary):
            direction, bottom_boundary, row, col = pivotLeft(row, col, direction, bottom_boundary, left_boundary)
            
        if direction == "left" and exceedingLeft(col, left_boundary):
            direction, left_boundary, row, col = pivotTop(row, col, direction, left_boundary, top_boundary)
        
        if direction == "top" and exceedingTop(row, top_boundary):
            direction, top_boundary, row, col = pivotRight(row, col, direction, top_boundary, right_boundary)
        
        # technically not required as length check used in while
        if (row, col) == (-1, -1):
            print("Issue")
            break
        spiral.append(array[row][col])
        spiral_length += 1
    return spiral

# get next point
def getNextPoint(direction, row, col):
	if direction == "right":
		return (row, col+1)
	if direction == "down":
		return (row+1, col)
	if direction == "left":
		return (row, col-1)
	if direction == "top":
		return (row-1, col)

# boundary checks
def exceedingRight(col, right_boundary):
	return col == right_boundary
def exceedingDown(row, bottom_boundary):
	return row == bottom_boundary
def exceedingLeft(col, left_boundary):
	return col == left_boundary
def exceedingTop(row, top_boundary):
	return row == top_boundary
	
# pivoting functions
def pivotDown(row, col, direction, right_boundary, bottom_boundary):
	print("pivotDown called")
	if exceedingDown(row+1, bottom_boundary):
		return (-1, -1)
	direction = "down"
	right_boundary = col-1
	return (direction, right_boundary, row+1, col-1)

def pivotLeft(row, col, direction, bottom_boundary, left_boundary):
	print("pivotLeft called")
	if exceedingLeft(col-1, left_boundary):
		return (-1, -1)
	direction = "left"
	bottom_boundary = row-1
	return (direction, bottom_boundary, row-1, col-1)

def pivotTop(row, col, direction, left_boundary, top_boundary):
	print("pivotTop called")
	if exceedingTop(col-1, top_boundary):
		return (-1, -1)
	direction = "top"
	left_boundary = col+1
	return (direction, left_boundary, row-1, col+1)

def pivotRight(row, col, direction, top_boundary, right_boundary):
	print("pivotRight called:", row, col)
	if exceedingRight(col+1, right_boundary):
		return (-1, -1)
	direction = "right"
	top_boundary = row+1
	return (direction, top_boundary, row+1, col+1)