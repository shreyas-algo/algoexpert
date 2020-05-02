# Approach: Go DFS & simplay keep swapping right with left
# O(N) time & O(1) space
# Status: all test cases accepted
def invertBinaryTree(tree):
    if tree == None:
        return
    swapChildren(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return

def swapChildren(tree):
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    return