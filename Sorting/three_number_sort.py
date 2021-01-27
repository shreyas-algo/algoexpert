# TODO: Solve using logic
# Approach: Used basic python method of sorting an array based on a key 
# Analysis: O(n log n) where n is size of array

def threeNumberSort(array, order):
    array.sort(key=lambda x: order.index(x))
	return array