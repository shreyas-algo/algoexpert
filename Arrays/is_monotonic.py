# check whether an array is strictly incresaing or strictly decreasing
# Approach: Get order pattern by checking first two unequal numbers. Then iterate the array again checking that all elements follow the same pattern (increasing or decreasing)
# Analysis: O(2N) = O(N)
def isMonotonic(array):
    arr_len = len(array)
    order = checkOrder(array, arr_len)
    for idx in range(arr_len-1):
        if order == "inc" and array[idx] < array[idx+1]:
            return False
        if order == "dec" and array[idx] > array[idx+1]:
            return False
    return True

# find whether the pattern is non-increasing or non-decreasing
def checkOrder(array, arr_len):
	for idx in range(arr_len-1):
		if array[idx] == array[idx+1]:
			# equality doesn't give decisive info
			continue
		elif array[idx] > array[idx+1]:
			return "inc"
		else:
			return "dec"
	# all values are same in array
	return "inc"

