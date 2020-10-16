# Approach: Draw on paper and observe that the zigzag traverse is nothing but a combination of plank-ups & plank-downs with one initalizing the start position of the other. Once you have a start position, plankUp or plankDown is simply going up/down until you are about to cross a boundary of the input matrix
# Analysis: O(row*col) time & O(row*col) space (for result)

# Questions to ask:
# 1. Does the input only have squares or should it also work for rectangles, single row, single column?

# Learning:
# 1. IMP: SIMPLIFY PROBLEM! Break a complex problem in an easier problem. eg broken down to plankUp & plankDown here
# 2. Solve a simpler version of the problem -- eg here solve just for squares and then expand your solution (eg solve just for thenfirst test case given)

def zigzagTraverse(array):
	res = []
	row = 0
	col = 0
	row_len = len(array)
	# edge case
	if row_len < 1:
		return res
	# considering symmetric shape
	col_len = len(array[0])
	# init first entry
	res.append(array[row][col])
	if row+1 < row_len:
		row += 1
	else:
		col += 1
	# plank functions - append values in current plank and init next plank's row, col
	while row < row_len and col < col_len:
		# plankUp will happen either from a left boundary or a bottom boundary
		if col == 0 or row == row_len-1:
			row, col = plankUp(array, row, col, row_len, col_len, res)
			print("Next PlankDown",row,col)
		# plankDown will happen either from a top boundary or a right boundary
    	elif row == 0 or col == col_len-1:
			row, col = plankDown(array, row, col, row_len, col_len, res)
			print("Next PlankUp",row,col)
	return res

def plankUp(array, row, col, row_len, col_len, res):
	# assignment to r,c not really required
	r = row
	c = col
	# an until loop 
    # this is more like a while True. The inside break is the actual condition that drives it. But this is to make sure that r & c never exceed bounds
	while r < row_len and c < col_len:
		print(r,c)
		res.append(array[r][c])
		# as soon as the plank reaches, top or right boundary, break
		if r == 0 or c == col_len-1:
			break
		r -= 1
		c += 1
	print("plankUp ends", r,c)
	# preference to right move, if available
	if c+1 < col_len:
		return (r,c+1)
	else:
		return (r+1,c)
		
def plankDown(array, row, col, row_len, col_len, res):
	# assignment to r,c not really required
	r = row
	c = col
	# an until loop 
	while r < row_len and c < col_len:
		res.append(array[r][c])
		# as soon as the plank reaches, bottom or left boundary, break
		if r == row_len - 1 or c == 0:
			break
		r += 1
		c -= 1
	print("plankDown ends", r,c)
	# preference to bottom move, if available
	if r+1 < row_len:
		return (r+1,c)
	else:
		return (r,c+1)
		
	