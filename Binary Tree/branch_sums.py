# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Status - Does not run succcesfully when "Run Tests" used on Algoexpert. But works when single test case is populated and checked
# Update: Added print and compared to test cases. It looks good. Possibly the issue is how Algoexpert is calling the function
# curr_sum = 0
# result = []
def branchSums(root, curr_sum=0, result=[]):
    if root.left == None and root.right == None:
        print("leaf: {}, sum: {}".format(root.value, curr_sum + root.value))
        result.append(curr_sum + root.value)
    if root.left != None:
        branchSums(root.left, curr_sum + root.value, result)
    if root.right != None:
        branchSums(root.right, curr_sum + root.value, result)
    return result