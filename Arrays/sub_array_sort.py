def subarraySort(array):
    start = -1
	end = -1
	arr_len = len(array)
	if arr_len < 1:
		return [-1, -1]
	# find first dip to initialize start
	# can done in one loop but this is better for code readability and abstraction
	# start - start index from where array needs to be sorted
	# end - end index until where array needs to be sorted
	# leftWall - right end (index) of the sorted array on left aka index of largest value tracked outside sub_array (to be sorted) on left 
	# maxInside - largest value tracked after the sub_array started
	
	start, end, leftWall, maxInside  = findFirstDip(array, arr_len)
	# if no dip found, it's already sorted
	if start == -1:
		return [-1, -1]
	
	print(start, end, leftWall, maxInside)
	for i in range(start, arr_len):
		# 1. update start until the largest number outside (maxOutside) is smaller than or equal to the number itself (array[i]) or start is set to 0
		if  start != 0 and array[i] < array[leftWall]:
			start, leftWall = goBackUntilSmaller(array, leftWall, array[i])
		# 2. update end if the current number is smaller than the max inside sub_array (it comes under range of sorted numbers)
		# also when updating end, check if maxInside needs to be updated
		if array[i] < maxInside:
			end = i
		# update maxInside
		if array[i] > maxInside:
			maxInside = array[i]
	return [start, end]

# O(n)
def findFirstDip(array, arr_len):
	for i in range(arr_len-1):
		if array[i] > array[i+1]:
			return (i+1,i+1,i,array[i+1])
	return (-1, -1, -1, -1)
		
# ~O(n)
def goBackUntilSmaller(array, leftWall, target):
	# reverse for loop on array from start to find a smaller numner than target
	for i in range(leftWall, 0, -1):
		if array[i] <= target:
			return (i, i-1)
	# if nothing smaller, set start to 0. 
	return (0, -1)
		