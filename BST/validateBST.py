# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Approach: check if the current structure is right and then left and right children are also validBSTs. If yes, overall it's a validBST
def validateBst(tree):
    if tree is None:
		return True
	if validBSTStructure(getMaxValue(tree.left), tree, getMinValue(tree.right)) and validateBst(tree.left) and validateBst(tree.right):
		return True
	else:
		print("returning false on: ", tree.value)
		return False

def validBSTStructure(left, root, right):
	if left is not None and left.value >= root.value:
		return False
	if right is not None and right.value < root.value:
		return False
	return True

# return right most value in a BST    
def getMaxValue(node):
    # if tree.left itself did not exist
    if node is None:
        return None
    # keep going right until possible
    if node.right is not None:
        getMaxValue(node.right)
    # if can't go right any further, return value. This will be the max
    return node.value

# return left most value in a BST    
def getMinValue(node):
    if node is None:
        return None
    # keep going left until possible
    if node.left is not None:
        getMinValue(node.left)
    return node.value
	
	
