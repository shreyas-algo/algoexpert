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
	row += 1
	# plank functions - append values in current plank and init next plank's row, col
	while row < row_len and col < col_len:
		if col == 0 or row == row_len-1:
			row, col = plankUp(array, row, col, row_len, col_len, res)
    	elif row == 0 or col == col_len-1:
			row, col = planDown(array, row, col, row_len, col_len, res)
	return res

def plankUp(array, row, col, row_len, col_len, res):
	r = row
	c = col
	# an until loop 
	while True:
		res.append(array[r][c])
		if r == col and c == row:
			break
		r -= 1
		c += 1
	# set next r,c 
	# reached final column
	if c == col_len-1:
		return (r+1,c)
	# reached top row - r == 0
	else:
		return (r,c+1)
		# Handled in parent while
		# if r+1 < row_len:
		# 	return (r+1,c)
		# Handled in parent while - mostly this case will never happen. This is like r==row_len-1 and c==col_len-1
		# return (r,c)
		
def planDown(array, row, col, row_len, col_len, res):
	r = row
	c = col
	# an until loop 
	while True:
		res.append(array[r][c])
		if r == col and c == row:
			break
		r += 1
		c -= 1
	# set next r,c 
	# reached first column
	if c == 0:
		return (r+1,c)
	# reached last row: r == row_col-1
	else:
		return (r,c+1)
		
		
	