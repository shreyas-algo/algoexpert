# Approach: break in a problem of num + threeSum (we know that threeSum can be solved in O(n*n))
# Analysis: O(n^3)

# TODO: Implement Algoexpert's solution of O(n^2): Sum of pairs

def fourNumberSum(array, targetSum):
    array.sort()
	end = len(array)
	four_sum_result = []
	for i, num in enumerate(array):
		threeSumTarget = targetSum - num
		results = threeNumberSum(array, i+1, end, threeSumTarget)
		print(threeSumTarget, results)
		# append current num to all results of three sum
		for res in results:
			# might need to change to appendLeft() if quadruplets required in order
			res.append(num)
			four_sum_result.append(res)
    return four_sum_result

def threeNumberSum(array, start, end, targetSum):
	result = []
	for i in range(start, end):
		target = targetSum - array[i]
		lo = i+1
		hi = end - 1
		while lo < hi:
			sum = array[lo] + array[hi]
			if sum == target:
				result.append([array[i], array[lo], array[hi]])
				lo += 1
				hi -= 1
			elif sum < target:
				lo += 1
			else:
				hi -= 1
	return result
	
