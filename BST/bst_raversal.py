# Approach: call recursively and keep updating the array. Look at it as a combination of nested calls. eg inorder(node) = inorder(node.left) + node + inorder(node.right)
# think of preorder first to ease process of thinking

# Learning: recursion child return propogation (using or returning value coming from a child case) is required in cases when child node returns the answer or a part of the answer) 
# But that is not required when you're using a separate variable to save your results.
# eg Notice that in this question as array variable always gets updated with the elements as we go on, you don't have to worry about what the intermeddiate recursive calls return
# For more info, look at previous commits of this file which work exactly the same even though there we collect the intermeddiate results of inOrderTraverse etc back in array variable

# O(n) time & O(d) space (recursion call stack) where d is max depth of tree
def inOrderTraverse(tree, array):
    if tree is None:
		return
	if tree.left is not None:
		inOrderTraverse(tree.left, array)
	array.append(tree.value)
	if tree.right is not None:
		inOrderTraverse(tree.right, array)
	return array


def preOrderTraverse(tree, array):
    if tree is None:
		return
	array.append(tree.value)
	if tree.left is not None:
		preOrderTraverse(tree.left, array)
	if tree.right is not None:
		preOrderTraverse(tree.right, array)
	return array
		

def postOrderTraverse(tree, array):
    if tree is None:
		return
	if tree.left is not None:
		postOrderTraverse(tree.left, array)
	if tree.right is not None:
		postOrderTraverse(tree.right, array)
	array.append(tree.value)
	return array

