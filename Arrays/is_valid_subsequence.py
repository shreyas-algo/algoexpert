from collections import deque
def isValidSubsequence(array, sequence):
	sequenceLength = len(sequence)
	arrayLength = len(array)
	# edge cases
	if sequenceLength == 0 or arrayLength == 0 or sequenceLength > arrayLength:
		return False
	
	# convert to deque in O(m) time to make popleft() constant time
	sequence_queue = deque(sequence)
	top = sequence_queue.popleft()
    for value in array:
		if value == top:
			if not sequence_queue:
				return True
			top = sequence_queue.popleft()
    return False
