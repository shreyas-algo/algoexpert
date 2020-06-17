# Approach II: 2 pointers start and end. End always stays on a swappable position & move array[start] if it doesn't match toMove. No need to loop through array. Use while condition. Cleaner code & O(N). No need to getLastSwappable position (as in Approach I). Use end increment accordingly
# Analysis: O(N) time, O(1) space

def moveElementToEnd(array, toMove):
    start = 0
    end = len(array) - 1
    while start < end:
        if array[end] == toMove:
            # if array[end] is already a target element, keep moving from behind until you reach a non-target element
            end -= 1
            continue
        if array[start] == toMove:
            swap(array, start, end)
            end -= 1
        start += 1
    return array

    def swap(array, idx, end):
        temp = array[idx]
        array[idx] = array[end]
        array[end] = temp



# Approach I: two pointer: start and end. look at start and swap with end if start != toMove. Shift both start and end accordingly 
# Analysis: O(N*N) time, O(1) space
# O(N*N) because getLastSwappablePosition() can take O(N) time in worst case -- Imagine a very long array with all the target elements in the middle. For every element, you'll run getLastSwappablePosition which will take ~O(N) time 

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

	