# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.
# same as twoNumberSum 
# targetSum: result - buffer
# array: array of song times
def twoNumberSum(array, targetSum):
    passed = {}
    indices = {}
    for idx, item in enumerate(array):
        diff = targetSum - item
        if diff in passed:
            return [indices[diff], idx]
    passed[item] = True
    indices[item] = idx
    return []