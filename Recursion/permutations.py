result = []
def getPermutations(array):
	if len(array) == 2:
		print([array[0], array[1]], [array[1], array[0]])
		return [[array[0], array[1]], [array[1], array[0]]]
    for integer in array:
		remaining = getPermutations(list(set(array) - set([integer])))
		for rem in remaining:
			rem.append(integer)
			result.append(rem)
    return result
