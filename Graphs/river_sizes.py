# Approach: whenever you encounter a 1 that's not visited, mark all possoble adjacent 1s and return size
# O(s) time & O(s) space where s is the size of the matrix

# Learning: whenever you see issue in recursion code, always check whether you're catching return from intermeddiate recursion call. It's a common mistake you make
# eg here the `size = markAdjacent()` part in `markAdjacent()`` internal calls. Notice that if you don't do this, the updated size value from #top will not take reflect in call made for right cz as the recursion returns to parent, the parent size will still be what was passed to it as an argument
def riverSizes(matrix):
    rowlen = len(matrix)
	collen = len(matrix[0])
	passed = set()
	result = []
    for row in range(rowlen):
		for col in range(collen):
			if (row,col) not in passed and matrix[row][col] == 1:
				size = markAdjacent(matrix, row, col, rowlen, collen, passed)
				result.append(size)
	return result

def markAdjacent(matrix, row, col, rowlen, collen, passed, size=0):
	passed.add((row,col))
	size += 1
	
	# top check
	if row - 1 >= 0 and (row-1,col) not in passed and matrix[row-1][col] == 1:
		size = markAdjacent(matrix, row-1, col, rowlen, collen, passed, size)
		
	# right check
	if col+1 < collen and (row,col+1) not in passed and matrix[row][col+1] == 1:
		size = markAdjacent(matrix, row, col+1, rowlen, collen, passed, size)
	
	# bottom check
	if row + 1 < rowlen and (row+1,col) not in passed and matrix[row+1][col] == 1:
		size = markAdjacent(matrix, row+1, col, rowlen, collen, passed, size)
		
	# left check
	if col-1 >= 0 and (row,col-1) not in passed and matrix[row][col-1] == 1:
		size = markAdjacent(matrix, row, col-1, rowlen, collen, passed, size)
	
	return size
	
	
