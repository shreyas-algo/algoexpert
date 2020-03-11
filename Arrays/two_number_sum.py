# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.

def twoNumberSum(array, targetSum):
    # brute force
    # length = len(array)
    # for idx in range(length):
    # 	for idx2 in range(idx+1, length):
    # 		if array[idx] + array[idx2] == targetSum:
    # 			return [array[idx], array[idx2]]

    # optimized: Keep a dictionary to store each number you're looking for and if you find it, just return the pair
    passed = {}
    for item in array:
        if targetSum - item in passed:
            return [item, targetSum - item]
    passed[item] = True
    return []