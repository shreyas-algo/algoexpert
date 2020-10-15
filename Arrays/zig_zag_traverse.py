# Approach:
# Analysis:

# Questions to ask:
# 1. Does the input only have squares or should it also work for rectangles, single row, single column?

# Learning:
# 1. Solve a simpler version of the problem -- eg here solve just for squares and then expand your solution (eg solve just for thenfirst test case given)

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
	matrix_len = row_len * col_len
	# init first entry
	res.append(array[row][col])
	row += 1
	# plank functions - append values in current plank and init next plank's row, col
	while row < row_len and col < col_len and len(res) <= matrix_len:
		if col == 0 or row == row_len-1:
			row, col = plankUp(array, row, col, row_len, col_len, res)
			print("Next PlankDown",row,col)
    	elif row == 0 or col == col_len-1:
			row, col = planDown(array, row, col, row_len, col_len, res)
			print("Next PlankUp",row,col)
	return res

def plankUp(array, row, col, row_len, col_len, res):
	r = row
	c = col
	# an until loop 
    # this is more like a while True. The inside break is the actual condition that drives it. But this is to make sure that r & c never exceed bounds
	while r < row_len and c < col_len:
		print(r,c)
		res.append(array[r][c])
		if r == 0 or c == col_len-1:
			break
		r -= 1
		c += 1
	print("plankUp ends", r,c)
	if c+1 < col_len:
		return (r,c+1)
	elif r+1 < row_len:
		return (r+1,c)
	else:
		return (r,c)
	# set next r,c 
	# reached final column
	# if c == col_len-1:
	# 	return (r+1,c)
	# # reached top row - r == 0
	# else:
	# 	return (r,c+1)
		# Handled in parent while
		# if r+1 < row_len:
		# 	return (r+1,c)
		# Handled in parent while - mostly this case will never happen. This is like r==row_len-1 and c==col_len-1
		# return (r,c)
		
def planDown(array, row, col, row_len, col_len, res):
	r = row
	c = col
	# an until loop 
	while r < row_len and c < col_len:
		res.append(array[r][c])
		if r == row_len or c == 0:
			break
		r += 1
		c -= 1
	print("plankDown ends", r,c)
	# set next r,c 
	# reached first column
	# if col == col_len-1:
	# 	return (r+1,c)
	# # reached last row: r == row_col-1
	# else:
	# 	return (r,c+1)
	if r+1 < row_len:
		return (r+1,c)
	elif c+1 < col_len:
		return (r,c+1)
	else:
		return (r,c)
		
	