# Approach: two pointer: start and end. look at start and swap with end if start != toMove. Shift both start and end accordingly 
def moveElementToEnd(array, toMove):
    end = getLastSwappablePosition(array, toMove)
    for idx, item in enumerate(array):
        print(array)
        print(idx,end)
        if idx >= end:
            break
        if item == toMove:
            swap(array, idx, end)
            end -= 1
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
	