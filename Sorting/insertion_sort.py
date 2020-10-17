# Approach: Keep left side of the array sorted. Start comparing each number by its immediate left neighbour (right end of the sorted array). If the 


# Learning:
# 1. Understanding the question nicely and drawing it out. Running a sample yourself with just the logic you have in mind. (you dont even need the whole algo written). Just running through an example (& then maybe one or two more) is crucial! Once you know your logic is rock-solid. You just gotta keep your drawings in front of you and visualize yur logic running over your example. The code will come super smooth and fast (eg writing sorting algos after seeing Algoexpert videos in ~5 minutes! Implementing Tries & Heaps cz the understanding was crystal clear)

def insertionSort(array):
	arr_len = len(array)
	# edge cases
	if arr_len < 2:
		return array
	
    for i in range(1, arr_len):
		if array[i] < array[i-1]:
			placeInSortedArray(array, i)
    return array

def placeInSortedArray(array, i):
	while i >= 1:
		if array[i] < array[i-1]:
			array[i], array[i-1] = array[i-1], array[i]
			i -= 1
		else:
			break