# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Approach: calculated sum in DFS fashion. Appened array on leaf nodes. Passed curr_sum as parameter
# Status - Does not run succcesfully when "Run Tests" used on Algoexpert. But works when single test case is populated and checked
# Update: Added print and compared to test cases. It looks good. Possibly the issue is how Algoexpert is calling the function
# Confirmed: The logic is right. Added a wrapper for the recursive call and it works for all test cases.

# O(n) time
# O(d) space due to recursive calls (where d is the max depth of the tree) and O(n/2) due to result array (A balanced tree can have at most n/2 leaves). If not balanced, then it's a single branch so O(1) for result but O(n) for recursive calls
# So effectively O(n) space
def branchSums(root, result=[], curr_sum=0):
	if root is None:
		return
	curr_sum = curr_sum + root.value
	if root.left is None and root.right is None:
		result.append(curr_sum)
		return
	branchSums(root.left, result, curr_sum)
	branchSums(root.right, result, curr_sum)
	return result


# --------------------------
# Solution for Algoexpert:
def branchSums(root):
    result = []
    addSumsToList(root, result, 0)
    return result
			   
def addSumsToList(root, result, curr_sum):
	if root is None:
		return
	curr_sum = curr_sum + root.value
	if root.left is None and root.right is None:
		result.append(curr_sum)
		return
	addSumsToList(root.left, result, curr_sum)
	addSumsToList(root.right, result, curr_sum)
	return result
