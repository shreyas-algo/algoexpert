# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value == -1:
        return evaluateExpressionTree(tree.left) + evaluateExpressionTree(tree.right)

    elif tree.value == -2:
        return evaluateExpressionTree(tree.left) - evaluateExpressionTree(tree.right)

    elif tree.value == -3:
        return int(evaluateExpressionTree(tree.left) / evaluateExpressionTree(tree.right))

    elif tree.value == -4:
        return evaluateExpressionTree(tree.left) * evaluateExpressionTree(tree.right)

    else:
        return tree.value
