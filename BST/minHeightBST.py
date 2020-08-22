def minHeightBst(array):
	# Note: Use deque for optimized popleft. Fine here as only used once
	arr_len = len(array)
	return insertionHelper(array, 0, arr_len)

def insertionHelper(array, lo, hi, root=None):
	if lo >= hi:
		return
	mid = int((lo+hi)/2)
	if root is None:
		root = BST(array[mid])
	else:
		root.insert(array[mid])
	insertionHelper(array, lo, mid, root)
	insertionHelper(array, mid+1, hi, root)
	return root

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
