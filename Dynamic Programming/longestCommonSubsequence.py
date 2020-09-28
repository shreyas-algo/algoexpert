# Approach: Create matrix that keeps track of longest subsequence using the strings up to str1[:i] & str2[:j] one character at a time. Notice '' & '' have length of 0 and common: ''. Build matrix one row / col at a time
# Also notice that if str1[i] == str[j], then resultant subsequence length is 1+result[row-1][col-1] (i.e ehetver was max without this char + 1)
# if not equal, then it's max of result[row][col-1] & result[row-1][col] (use one of the characters whichever results in longest subsequence)
# USe resultant_string to also keep track of the resultant string at every position in the matrix
# Analysis: O(n*m) time & O(n*m) space where n & m are lengths of strings

# TODO: Watch video
# TODO: Think: Can you do this with one matrix? -- might increase time -- can you do it without adding extra time

def longestCommonSubsequence(str1, str2):
    # init
    # keeps track of max length of sub sequence at location i,j
	result = []
    # keeps track of longest subsequence using the strings up to str1[:i] & str2[:j]
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
				longer_row, longer_col = (row,col-1) if result[row][col-1] > result[row-1][col] else (row-1,col)
				result[row].append(result[longer_row][longer_col])
				resultant_string[row].append(resultant_string[longer_row][longer_col])
	print(resultant_string)
	return list(resultant_string[len_1][len_2])
			
