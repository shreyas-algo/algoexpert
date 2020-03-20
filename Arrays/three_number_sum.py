def threeNumberSum(array, targetSum):
    result = []
	length = len(array)
	array.sort()
	for idx in range(length-1):
		target = targetSum - array[idx]
		expected = set()
		for idx2 in range(idx+1, length):
			if array[idx2] in expected:
				result.append([array[idx], target - array[idx2], array[idx2]])
			expected.add(target - array[idx2])
    return sorted(result)