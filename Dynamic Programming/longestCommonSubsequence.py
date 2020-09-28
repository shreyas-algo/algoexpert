def longestCommonSubsequence(str1, str2):
    # init
	result = []
	resultant_string = []
	# keeps track of string formed at every [row][col]
	tracker = {}
	len_1 = len(str1)
	len_2 = len(str2)
	for row in range(len_1+1):
		for col in range(len_2+1):
			if col == 0:
				# initialize the new row 
				result.append([0])
				resultant_string.append([''])
				continue
			if row == 0:
				# initialize contents of the first row
				result[0].append(0)
				resultant_string[0].append('')
				continue
			
			# print(row, col)
			if str1[row-1] == str2[col-1]:
				result[row].append(1 + result[row-1][col-1])
				resultant_string[row].append(resultant_string[row-1][col-1] + str1[row-1])
			else:
				longer_row, longer_col = (row,col-1) if result[row][col-1] > result[row-1][col] else (row,col-1)
				result[row].append(result[longer_row][longer_col])
				resultant_string[row].append(resultant_string[longer_row][longer_col])
			
	print(resultant_string[len_1][len_2])
	return list(resultant_string[len_1][len_2])
			
