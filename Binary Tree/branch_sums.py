# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Approach: calculated sum in DFS fashion. Appened array on leaf nodes. Passed curr_sum as parameter
# Status - Does not run succcesfully when "Run Tests" used on Algoexpert. But works when single test case is populated and checked
# Update: Added print and compared to test cases. It looks good. Possibly the issue is how Algoexpert is calling the function

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
