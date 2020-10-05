# Approach: sort & go through array checking immediate neighbours & updating largestRange if a larger range is found
# O(n log n) time & O(1) space
def largestRange(array):
	arr_len = len(array)
	array.sort()
	# edge case
	if arr_len < 1:
		return [-1, -1]
	# result realted vars
    res_start = 0
	res_end = 0
	max_len = 1
	# loop tracking vars
	curr_start = 0
	curr_end = 0
	print(arr_len)
	for i in range(1, arr_len):
		# continuous numbers or same number 
		print(array[i] - array[i-1] )
		if array[i] - array[i-1] == 1 or array[i] - array[i-1] == 0:
			curr_end = i
		else:
			curr_len = array[curr_end] - array[curr_start] + 1
			# equality depends on how the interviewer wants it. If they want the last found range or the first first found range if there are two loargest ranges
            # notice that question mentions that there is only single largest range in the inputs but Test Cse #7 breaks without equality
            # TODO: check failing cases by removing equality and leave feedback for quesiton if you're right. Equality is important if there can be multiple
            # [-1, 8] & [10, 19] -- 2 ranges exist with length 10
            if curr_len >= max_len:
				# update result related vars
				max_len = curr_len
				res_start = curr_start
				res_end = curr_end
				# update iteration tracking vars
				curr_start = i
				curr_end = i
	curr_len = array[curr_end] - array[curr_start] + 1
	if curr_len >= max_len:
		return [array[curr_start], array[curr_end]]
    return [array[res_start], array[res_end]]
