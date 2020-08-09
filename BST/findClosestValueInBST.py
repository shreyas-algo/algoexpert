# Approach I: Go through the tree in find_in_BST fashion but also keep track of closest value & mindiff as you're going through. Keep updating closest on every call. Finally return closest
# Analysis: O(log N)

# TODO: Watch Algoexpert solution

# BIG Learning (To remember):
# recursion propogates from base case up to the parent. It's the parent call that returns finally. 
# So always return result from your child call and use it in the parent call to return answer
# IMP: See lines 19 & 21 where you're updating `closest` value based on what the child branch returns. 
    # That is crucial. If you do not do that, the child will update closest but the closest value will not propogate up to the parent call and the parent call will return a stale closest

# Approach II: Notice that the closest number to a node will be the smallest number in its right subtree or largest element in its left subtree (draw and check)

def findClosestValueInBst(tree, target, minDiff=1000000, closest=None):
    if tree.value == target:
		return tree.value
	if abs(tree.value - target) < minDiff:
		minDiff = abs(tree.value - target)
		closest = tree.value
	if tree.value < target and tree.right:
		closest = findClosestValueInBst(tree.right, target, minDiff, closest)
	elif tree.left:
		closest = findClosestValueInBst(tree.left, target, minDiff, closest)
    # if no branch left to explore
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
