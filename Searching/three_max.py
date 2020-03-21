# Approach I: Sort and return last 3
# O (NlogN)

# Approach II: Do a single pass and maintain a max-array of size three. Check every element in the array with the max-array and maintain highest 3 at all times
# O (N)
import sys
def findThreeLargestNumbers(array):
	# init
	length = len(array)
	min_int = -sys.maxsize - 1  # -9223372036854775808
	# todo: change if to assert
	if length > 2:
		max_array = sorted([array[0], array[1], array[2]], reverse=True)	# sorting 3 numbers in some constant time: 3 log 3
		print(max_array)
		max_array.append(min_int)	# create temp slot for compare
		# todo: optimize: use index instead of slice. Slice is O(N)
		for item in array[3:]:
			# minor optimization: check only if the incoming number is at least higher than the least element in the max-array
			if item > max_array[3]:
				max_array[3] = item
				max_array = sorted(max_array, reverse=True)
		print(max_array)
		return max_array[2::-1]	# remember: slicing takes O(N) time because it's a copy operation but here, ok, coz only done once
	return "Expecting at least 3 values"