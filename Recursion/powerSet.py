# Approach: for every element in array, add element and recursively call the power_set function for the remaining set (excluding the integer)
# TODO: Optimization: Use key creation and storing instead of using tuples as keys for list. As list -> tuple is a O(N) operation

# result: list holding result
# power_set: set holding passed values
# TODO: consider doing with a single set
def powerset(array, result = [], power_set = set()):
    # add the whole array itself
	if tuple(array) not in power_set:
		result.append(array)
		power_set.add(tuple(array))
    
    # iterate over every element
	for integer in array:
        # if integer not added, add
		if tuple([integer]) not in power_set:
			result.append([integer])
			power_set.add(tuple([integer]))
        # find set difference & call recursively if not yet added
		remaining = list(set(array) - set([integer]))
		if tuple(remaining) not in power_set:
			powerset(remaining, result, power_set)
			power_set.add(tuple(remaining))
	return result
