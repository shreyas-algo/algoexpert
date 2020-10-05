# Approach: sort & go through array checking immediate neighbours & updating largestRange if a larger range is found
    # init curr_start & curr_end
    # update curr_start whenever a sequence breaks
    # update curr_end whenever the condition satisfies (difference is 1 or 0). curr_end not necessary. can work with i but just kept for cleaner, readable code
    # keep track of curr_len, curr_start, curr _end for current sequence range & update max_len, res_start & res_end when we find a larger range
    # Note: when calculating length, use array[start/end] (values) & not start, end to diffrentiate between sequences that have duplicate numbers and sequences that actually have higher range. eg [1,1,1,2] vs [3,4,5] range(3,4,5) = 3 whereas range(1,1,1,2) = 2 even though it's length of number is higher
# O(n log n) time & O(1) space

# TODO: watch video
def largestRange(array):
	arr_len = len(array)
	array.sort()
	# edge case
	if arr_len < 1:
		return [-1, -1]
	# result related vars
    res_start = 0
	res_end = 0
	max_len = 1
	# loop tracking vars
	curr_start = 0
	curr_end = 0
	print(arr_len)
	for i in range(1, arr_len):
		# continuous numbers or same number 
		if array[i] - array[i-1] == 1 or array[i] - array[i-1] == 0:
			curr_end = i
		else:
            # imp: when calculating length of range, use values
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
    # check again in case it never updated inside (largestRange includes last number)
	curr_len = array[curr_end] - array[curr_start] + 1
	if curr_len >= max_len:
		return [array[curr_start], array[curr_end]]
    return [array[res_start], array[res_end]]
