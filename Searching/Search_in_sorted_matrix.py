def searchInSortedMatrix(matrix, target):
    # Approach I: Binary search on every row's elements
	# O (r * log c)
	
	# Approach II: Sliding window concept on a matrix
    # start with top-right corner. Make a move below or left accordingly until you reach element or grow out of matrix
	# O (r + c): r - number of rows; c - number of columns
	row = len(matrix) - 1
	col = len(matrix[0]) - 1		# Add safe checks of having at least one row
	r, c = 0, col
	while r <= row and c >= 0:		# while you're in the bounds of the matrix, keep checking
		if matrix[r][c] == target:
			return [r, c]
		elif matrix[r][c] <= target:
			r += 1
		else:
			c -= 1
	return [-1, -1]