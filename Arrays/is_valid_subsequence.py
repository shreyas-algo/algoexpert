# Approach: iterate over the array while checking one character at a time from the sequence (while also popping from the sequence) If nothing left to find in sequence, then return True else False
# Analysis: O(m) time & O(n) space (deque) where m is the length of the subsequence & n length of array

# Deque used to improve popLeft. Can also try a solution by iterating sequences in reverse. so that pop() itself can be used on the list

# TODO: Create constant space solution by iterating in reverse
# TODO: Look at video

from collections import deque
def isValidSubsequence(array, sequence):
	sequenceLength = len(sequence)
	arrayLength = len(array)
	# edge cases
	if sequenceLength == 0 or arrayLength == 0 or sequenceLength > arrayLength:
		return False
	
	# convert to deque in O(m) time to make popleft() constant time
	sequence_queue = deque(sequence)
	# get top element from subsequence & remove from sequence
	top = sequence_queue.popleft()
    for value in array:
		if value == top:
			# if nothing more left to search, subsequence found
			if not sequence_queue:
				return True
			# update top to be searched
			top = sequence_queue.popleft()
	# if by the end of it, if something left in top that couldn't be found, not a subsequence
    return False
