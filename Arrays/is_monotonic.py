# check whether an array is non-incresaing or  non-decreasing
# non-incresaing: strictly increasing or some values equal

# Approach: Get order pattern by checking first two unequal numbers. Then iterate the array again checking that all elements follow the same pattern (increasing or decreasing)
# Analysis: O(2N) = O(N)

# Learning: smart use of continue inside a loop to simulate a pseudo loop

def isMonotonic(array):
    arr_len = len(array)
    order = checkOrder(array, arr_len)
    for idx in range(arr_len-1):
        if order == "non-dec" and array[idx] < array[idx+1]:
            return False
        if order == "non-inc" and array[idx] > array[idx+1]:
            return False
    return True

# find whether the pattern is non-increasing or non-decreasing
def checkOrder(array, arr_len):
	for idx in range(arr_len-1):
		if array[idx] == array[idx+1]:
			# equality doesn't give decisive info
			continue
		elif array[idx] > array[idx+1]:
			return "non-dec"
		else:
			return "non-inc"
	# all values are same in array
	return "non-dec"

