# Approach: 
# Build a result array which stores result at every index (max sum with no alternates until index i) 
# Process:
# Compare array[i]+result[i-2] with result[i-1] and set the larger value as result[i]. Initialize result array with [array[0], array[1]]

# Logic: if every index' value is a valid result, then current item (array[i]) can only be included in result[i] with result[i-2] cz result[i-1] may have array[i-1] included and we need to avoid adjacent elements. In case array[i-1] is not included in result[i-1], result[i-1] will be same as result[i-2] (max logic) so result[i-1] is covered in final value of result[i]
# For example:
# array:    [100   1       99      100]
# result:   [100   100     199     200]

# Analysis: O(n) time and O(n) space

# IMP Learnings:
# 1. HINTS! They are there for the taking. Ask for help and hints if you can't breach a problem. 
# It's much BETTER than bombing the inteview and not making any progress
# Background: Was easily able to solve this question when read HINT #1: Try to create a solution array where at each index you store the maximum possible sum (by using alternate elements) until that index
# -
# 2. Dynamic Programming crux:
# Solve smaller problems and use the solution of the subset to solve a bigger problem
# Start thinking from smallest problem size and grow ahead. Almost opposite to recursion where you think for n and in the end decide base case

# TODO: Possible optimizstion on O(n) space: Keep only three elements. You don't need the full array

def maxSubsetSumNoAdjacent(array):
	# aedge cases
	arr_len = len(array)
	if arr_len == 0:
		return 0
	if arr_len == 1:
		return array[0]
	elif arr_len == 2:
		return max(array[0], array[1])
	# init
	result = []
	result.append(array[0])
	result.append(max(array[0], array[1]))
    # go over remaining array (skipping first two elements)
    for idx in range(2, len(array)):
		next_item = max(array[idx]+result[idx-2], result[idx-1])
		result.append(next_item)
	# return final element
	return result.pop()
