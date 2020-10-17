# Approach: Place the min at the front of array in each iteration. In n iterations, all n mins will be placed
# Analysis: O(n*n) time & O(1) space

def selectionSort(array):
    arr_len = len(array)
	for i in range(arr_len-1):
		# initialize min_idx
		min_idx = i
		for j in range(i+1,arr_len):
			if array[j] < array[min_idx]:
				min_idx = j
        # swap min from unsorted array with the current index to make the current index a part of the sorted sub array on left
		array[i], array[min_idx] = array[min_idx], array[i]
    return array
