# Approach: Iterate through the array and keep swapping a number at i with i+1 until you can find inversions ([i] > [i+1]). The moment you don't do any swaps, break out. Notice that on every iteration, the largest number will be placed at the last
# Analysis: O(n*n) time & O(1) space

# TODO: can add the minor optimization where you do not check the number placed at last cz you anyway know it is in its right place

def bubbleSort(array):
	arr_len = len(array)
	while True:
		swap = False
    	for i in range(arr_len-1):
			# check adjacent number
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				swap = True
		# if no swap happened, you have sorted the array
		# this will run at maxx O(n*n) times because at every iteration, you'll place the largest number at the back
		if swap == False:
			break
    return array
