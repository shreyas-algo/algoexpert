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
		if col == 0 or row == n:
			row, col = plankUp(array, row, col)
    	elif row == 0 or col == n:
			row, col = planDown(array, row, col)
	return res