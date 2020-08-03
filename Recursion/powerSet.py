result = []
# TODO: consider doing with a single set
power_set = set()
def powerset(array):
	if tuple(array) not in power_set:
		result.append(array)
		power_set.add(tuple(array))
	for integer in array:
		if tuple([integer]) not in power_set:
			result.append([integer])
			power_set.add(tuple([integer]))
		remaining = list(set(array) - set([integer]))
		if tuple(remaining) not in power_set:
			powerset(remaining)
			power_set.add(tuple(remaining))
	return result