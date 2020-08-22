# Approach: Keep calling the function with new depth on every level and keep track of sumDepth
# O(n) time and O(d) space where d is max depth

# TODO: Look at Algoexpert video
# TODO: Keep iterative solution from Algoexpert
# Learning: 
# When an array is involved, you don't need to propogate child results eg see branch_sums.py
# Whereas when it's a variable you need to because whatever happened in child calls, the parent is unaware of it
def nodeDepths(root, depth=0, sumDepth=0):
    if root is None:
		return sumDepth
	sumDepth += depth
	sumDepth = nodeDepths(root.left, depth+1, sumDepth)
	sumDepth = nodeDepths(root.right, depth+1, sumDepth)
    # finally
	return sumDepth

# -------------- Provided base class
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
