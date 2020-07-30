# Approach: Iterate through the array and for every element, append the element in the permutations of {array - element}. Thus `perm(contains: n) = perm(without n) + n` thus it is recursive definition with base case being only 2 elements when the result is {a, b} & {b ,a}
# Optimize: Memoize results

result = []
def getPermutations(array):
	if len(array) == 2:
		return [[array[0], array[1]], [array[1], array[0]]]
    for integer in array:
        # get all permutations except current integer
		remaining = getPermutations(list(set(array) - set([integer])))
        # append current integer in all results
		for rem in remaining:
			rem.append(integer)
			result.append(rem)
    return result
