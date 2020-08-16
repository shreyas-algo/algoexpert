# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    if tree is None:
		return True
	if validBSTStructure(tree.left, tree, tree.right) and validateBst(tree.left) and validateBst(tree.right):
		return True
	else:
		return False