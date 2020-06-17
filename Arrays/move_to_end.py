# Approach: two pointer: start and end. look at start and swap with end if start != toMove. Shift both start and end accordingly 
# Analysis: O(N) time, O(1) space

def moveElementToEnd(array, toMove):
    end = getLastSwappablePosition(array, toMove)
    for idx, item in enumerate(array):
        if idx >= end:
            break
        if item == toMove:
            swap(array, idx, end)
            end = getLastSwappablePosition(array, toMove)   # Old bug: end -= 1
    return array

def swap(array, idx, end):
	temp = array[idx]
	array[idx] = array[end]
	array[end] = temp

# get last postion of a non-target item in a list
# returns 0 if everything matches target
def getLastSwappablePosition(array, target):
	for idx in reversed(range(len(array))):
		if array[idx] != target:
			return idx
	# typically should be -1 : as it denotes no match found. But implemented this way to reduce extra logic in parent call
	return 0

# Important: Test case breaking:
# {"array": [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], "toMove": 5}
# Notice line 11: `end -= 1` and the problem is after a swap the last swappable position need not be end -1 coz end-1 may be a target element itslef!
# Learning: Need to be careful while coding. Do not just write stuff taking reference from old problems you've sold. Make sure what you write makes sense!

	