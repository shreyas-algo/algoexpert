# Approach: for every element in array, add element and recursively call the power_set function for the remaining set (excluding the integer)
# TODO: Optimization: Use key creation and storing instead of using tuples as keys for list. As list -> tuple is a O(N) operation
# TODO: Do preformance analysis 

# TODO: Understand and implement AlgoExpert's solution also
# Status: Working for all cases when individually populated but not for "all tests". Read the FAQ regarding this which said do not use global var and thus chnanged code. Still facing issue. Contacted AlgoExpert

# IMP Learning :
# Do not use Gloabl variables. Use local vars inside a function. If you need something to persist across function calls, use instantiated local params like used here `func(var=1)` (this means if var is passed it will take the value whatever is passed. if not, it will be initialized by 1)

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
