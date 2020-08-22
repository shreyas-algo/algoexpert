# Approach: Notice that when you insert mid element from a sorted array, you always end up with a min-height binary tree. So basically it becomes a question of extracting all elements from the array in a mid-first fashion. Basically leading to a binary search type approach. 
# Get mid and insert in BST root (if root is None, assign root). Then call insertion on left & right which does the same thing recursively
# O(n) time & O(n) space (call stack. n/2 to be precise)

# IMP Learning: 
# Binary Search important pointers:
# 1. init: lo = 0, hi = arr_len - 1
# 2. Base condition: `if lo > hi: return` --> i.e run `while lo <= hi` : Notice that the two conditions are complimentary but used differently. One breaks the recursion and other continues the iteration -- crux is run until lo == hi
# Basically the values always run on indices. ie. len-1 as hi, NOT len 
# And end on lo == hi (single element array)

def minHeightBst(array):
	# Note: Use deque for optimized popleft. Fine here as only used once
	arr_len = len(array)
	return insertionHelper(array, 0, arr_len-1)

def insertionHelper(array, lo, hi, root=None):
	if lo > hi:
		return
	mid = int((lo+hi)/2)
	if root is None:
		root = BST(array[mid])
	else:
		root.insert(array[mid])
	insertionHelper(array, lo, mid-1, root)
	insertionHelper(array, mid+1, hi, root)
	return root

# Helpers. Provided by default:
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

