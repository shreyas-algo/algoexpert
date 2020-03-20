# Approach used: Break dowmn in a problem of two-sum. For every number, create a 2_sum_target (called target in code) which you look for in the remaining array. The question basically becomes n iterations of two-sum
# Sort & sorted() used to satisfy the given condition of result array being sorted

def threeNumberSum(array, targetSum):
    result = []
	length = len(array)
	array.sort()
	for idx in range(length-1):
		target = targetSum - array[idx]
		passed = set()
		for idx2 in range(idx+1, length):
			if target - array[idx2] in passed:
				result.append([array[idx], target - array[idx2], array[idx2]])
			passed.add(array[idx2])
    return sorted(result)