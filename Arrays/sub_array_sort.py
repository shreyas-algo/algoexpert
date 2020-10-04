# Approach: Keep track of start & end by following
    # start: keep track of leftWall (index just before the sorting broke), update it if at any point you find a number if it's smaller than array[leftWall] because [leftWall] is basically the largest value in the sorted array on left (Also note that leftWall can't go further left than 0 i.e start will be at 0 after which any left shift is not possible)
    # init: findFirstDip - find the first point from where the sort pattern breaks for starters and initialize tracking vars like start, end, leftWall & maxInside
# Analysis: O(n^2) time worst case. & O(1) space

# TODO: write approach
# TODO: watch video

# Learnings:
# 1. Importance of Abstraction: When you can modularize the problem without hurting your asymptotic analysis. Do that! eg using findFirstDip() here to simplify the problem and initialize stuff. It could have been handled inside the main for loop but it would have complicated code and reduced readability
# 2. BIG: Writing function signature: It is important and it extremely helps to write a function signature over it (params & returns). (Especially when working with >1 return values) 
# It helps: 
# I) keeping track of what we're trying to achieve with the function 
# II) avoiding silly mistakes like flipping the order of return values or off-by-one errors
# you can also use some extra vars if it makes the code readable. eg leftWall here which will essentially be (start-1)

def subarraySort(array):
	arr_len = len(array)
	if arr_len < 1:
		return [-1, -1]
	# find first dip to initialize start
	# can done in one loop but this is better for code readability and abstraction
	# start - start index from where array needs to be sorted
	# end - end index until where array needs to be sorted
	# leftWall - right end (index) of the sorted array on left aka index of largest value tracked outside sub_array (to be sorted) on left 
	# maxInside - largest value tracked after the sub_array started
	
	# O(n) in worst case (sorted array) but in that case, we return out
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
# Finds start of the break in sorted pattern 
# and returns start, end, leftWall, maxInside
def findFirstDip(array, arr_len):
	for i in range(arr_len-1):
		if array[i] > array[i+1]:
			return (i,i,i-1,array[i])
	return (-1, -1, -1, -1)
		
# ~O(n)
# returns start (start of sub_array) & leftWall
def goBackUntilSmaller(array, leftWall, target):
	# reverse for loop on array from start to find a smaller numner than target
	for i in range(leftWall, -1, -1):
		if array[i] <= target:
			# which means leftWall found at i -- which means sub_array starts at i+1
			return (i+1, i)
	# if nothing smaller, set start to 0. 
	return (0, 0)
		