# TODO: Watch video

# Approach: Used basic python method of sorting an array based on a key 
# Analysis: O(n log n) where n is size of array

# Learnings:
# 0. IMP: When a desired order (or sorting result) given and the guarantee that each element in array will have an entry in order, solution possible in O(n)
# 1. Sorting an array based on values / indices of another array
# 2. Important thing to note here: Complexity is still mostly dependent on complexity of sort here because secondary array is constant size (3). or else the .index() will also contrbute O(m) where m is length of secondary array

# Questions to ask:
# 1. Will the order be necessarily increasing or decreasing - NO eg desired order can be [0, 1, -1] (arbitrary order)

# Approach III: count occurences of each item and place in order one by one
# O(n) time, O(1) space
# note that count_dict takes O(1) space as it will have at max 3 entries
def threeNumberSort(array, order):
    count_dict = count_occurences(array, order)
	start = 0
	for item in order:
		count = count_dict.get(item, 0)
		end = start + count
		place_item_in_correct_place(array, start, end, item)
		start = end
	return array

def count_occurences(array, order):
	count_dict = {}
	for item in array:
		existing_val = count_dict.setdefault(item, 0)
		count_dict[item] = existing_val + 1
	return count_dict

def place_item_in_correct_place(array, start, end, item):
	for i in range(start, end):
		array[i] = item
	
# ---

# Approach I:
def threeNumberSort(array, order):
    array.sort(key=lambda x: order.index(x))
	return array

# ---

# Approach II:
# Use modified sort algorithm to perform comparison based on order array
# Analysis: O(n*n)
def threeNumberSort(array, order):
    return selectionSort(array, order)

def selectionSort(array, order):
    arr_len = len(array)
	for i in range(arr_len-1):
		# initialize min_idx
		min_idx = i
		for j in range(i+1,arr_len):
            # key change -- in the decision making process, instead of comparing values in array use order in order array
			if order.index(array[j]) < order.index(array[min_idx]):
				min_idx = j
        # swap min from unsorted array with the current index to make the current index a part of the sorted sub array on left
		array[i], array[min_idx] = array[min_idx], array[i]
    return array
