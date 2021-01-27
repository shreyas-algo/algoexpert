# Approach: Used basic python method of sorting an array based on a key 
# Analysis: O(n log n) where n is size of array

# Learnings:
# 1. Sorting an array based on values / indices of another array
# 2. Important thing to note here: Complexity is still mostly dependent on complexity of sort here because secondary array is constant size (3). or else the .index() will also contrbute O(m) where m is length of secondary array

# Questions to ask:
# 1. Will the order be necessarily increasing or decreasing - NO eg desired order can be [0, 1, -1] (arbitrary order)

# Approach I:
def threeNumberSort(array, order):
    array.sort(key=lambda x: order.index(x))
	return array


# Approach II:
# Use modified sort algorithm to perform comparison based on order array
# Analysis: O(n*n)
def threeNumberSort(array, order):
    return selectionSort(array, order)

def selectionSort(array, order):
    arr_len = len(array)
	for i in range(arr_len-1):
		# initialize min_idx
		min_idx = i
		for j in range(i+1,arr_len):
            # key change -- in the decision making process, instead of comparing values in array use order in order array
			if order.index(array[j]) < order.index(array[min_idx]):
				min_idx = j
        # swap min from unsorted array with the current index to make the current index a part of the sorted sub array on left
		array[i], array[min_idx] = array[min_idx], array[i]
    return array
