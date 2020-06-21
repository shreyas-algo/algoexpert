# Approach II: Keep appending matrix boundary until available. Move to inner matrix once outer boundary done
# less complicated code
# O(N) time [N - total elements in matrix] & O(N) space [to store the result spiral]

# Learning: Think multiple ways to solve a problem. Also, it's better to work with index equality sometimes
# Note: Following code doesn't work for two edge cases: a) when there's single row left in middle (3x4 matrix) b) when there's single column in the middle of the matrix. Happens because when sRow=eRow & single row, both topRow printer & bottomRow printer will print first element
# Possible solutions:
# a) keep check on spiral_length == array_len and check this every time you append in spiral to avoid duplicates
# b) add single row & single column specific condition in bottomRow & leftColumn printer: `if sRow == eRow: break` 

# TODO: Overall improved approach: If you need to approach this porblem with a solution which is both clean and correct without missing edge cases:
# a) Implement perimeter solution
# b) keep the while check based on spiral length (can avoid abstraction. not required per se)

def spiralTraverse(array): 
    sRow = 0
    eRow = len(array)-1
    sCol = 0
    eCol = len(array[0])-1
    spiral = []
    # sprial_len = 0
    while sRow <= eRow and sCol <= eCol:
        appendTopRow(sRow, sCol, eCol, array, spiral)
        appendRightCol(eCol, sRow+1, eRow, array, spiral)
        appendBottomRow(eRow, eCol-1, sCol, array, spiral)
        appendLeftCol(sCol, eRow-1, sRow+1, array, spiral)
        # move to inner matrix
        sRow += 1
        sCol += 1
        eRow -= 1
        eCol -= 1
    return spiral

    def appendTopRow(sRow, sCol, eCol, array, spiral):
        while sCol <= eCol:
            spiral.append(array[sRow][sCol])
            sCol += 1

    def appendRightCol(eCol, sRow, eRow, array, spiral):
        while sRow <= eRow:
            spiral.append(array[sRow][eCol])
            sRow += 1

    def appendBottomRow(eRow, eCol, sCol, array, spiral):
        while eCol >= sCol:
            spiral.append(array[eRow][eCol])
            eCol -= 1
        
    def appendLeftCol(sCol, eRow, sRow, array, spiral):
        while eRow >= sRow:
            spiral.append(array[eRow][sCol])
            eRow -= 1
	


# Approach I: 
# * Draw on paper while keeping row & column header to visualize what is happening
# * Keep track of boundaries on all 4 sides and when a boundary is hit, change direction clockwise (for spiral) and update row, col accordingly

# Analysis: O(MxN)  [Matrix size]
# Remark: GREAT! Solved using clean abstracted code

# Learning: string, int & tuple parameters are passed-by-value whereas dictionaries, lists etc are passed-by-reference i.e when we change the argumemt in function, it is changed in the parent where it is called
# TODO: Watch video on Algoexpert

def spiralTraverse(array):
    matrix_len = len(array) * len(array[0])
    # init
    direction = "right"
    row, col = 0, 0
    # boundaries
    top_boundary = 0    # coz row: 0 is being printed initially
    left_boundary = -1  # coz left (col: 0) will need to be printed so the init left boundary is left of matrix' left i.e. -1
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
	if exceedingDown(row+1, bottom_boundary):
		return (-1, -1)
	direction = "down"
	right_boundary = col-1
	return (direction, right_boundary, row+1, col-1)

def pivotLeft(row, col, direction, bottom_boundary, left_boundary):
	if exceedingLeft(col-1, left_boundary):
		return (-1, -1)
	direction = "left"
	bottom_boundary = row-1
	return (direction, bottom_boundary, row-1, col-1)

def pivotTop(row, col, direction, left_boundary, top_boundary):
	if exceedingTop(col-1, top_boundary):
		return (-1, -1)
	direction = "top"
	left_boundary = col+1
	return (direction, left_boundary, row-1, col+1)

def pivotRight(row, col, direction, top_boundary, right_boundary):
	if exceedingRight(col+1, right_boundary):
		return (-1, -1)
	direction = "right"
	top_boundary = row+1
	return (direction, top_boundary, row+1, col+1)