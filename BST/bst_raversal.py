# Approach: call recursively and keep updating the array. Look at it as a combination of nested calls. eg inorder(node) = inorder(node.left) + node + inorder(node.right)
# think of preorder first to ease process of thinking

# O(n) time & O(n) space
def inOrderTraverse(tree, array):
    if tree is None:
		return
	if tree.left is not None:
		array = inOrderTraverse(tree.left, array)
	array.append(tree.value)
	if tree.right is not None:
		array = inOrderTraverse(tree.right, array)
	return array


def preOrderTraverse(tree, array):
    if tree is None:
		return
	array.append(tree.value)
	if tree.left is not None:
		array = preOrderTraverse(tree.left, array)
	if tree.right is not None:
		array = preOrderTraverse(tree.right, array)
	return array
		

def postOrderTraverse(tree, array):
    if tree is None:
		return
	if tree.left is not None:
		array = postOrderTraverse(tree.left, array)
	if tree.right is not None:
		array = postOrderTraverse(tree.right, array)
	array.append(tree.value)
	return array
