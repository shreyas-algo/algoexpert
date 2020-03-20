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
    return result