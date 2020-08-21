# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Approach: check if the current structure is right and then left and right children are also validBSTs. If yes, overall it's a validBST
# Learning: IMP: Repeating mistake:
# Propogating return from a recursive call: Using return on a recursive call is important to make the child calls affect the parent call return. Eg it will be `return getMaxValue(node.right)` and not simply `getMaxValue(node.right)`. Think about the reason

def validateBst(tree):
    if tree is None:
		return True
	if validBSTStructure(getMaxValue(tree.left), tree, getMinValue(tree.right)) and validateBst(tree.left) and validateBst(tree.right):
		return True
	else:
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
        return getMaxValue(node.right)
    # if can't go right any further, return. This will be the max
    return node

# return left most value in a BST    
def getMinValue(node):
    if node is None:
        return None
    # keep going left until possible
    if node.left is not None:
        return getMinValue(node.left)
    return node
	
	
