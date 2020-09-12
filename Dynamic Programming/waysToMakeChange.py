def numberOfWaysToMakeChange(n, denoms):
	# edge case
	if len(denoms) == 0:
		return 0
	# ways stores number of ways to store a value i
	ways = []
	# calculated keeps track of pairs for which ways have already been added
	# just declared here for saving space. re init in findWays function
	calculated = set()
	# initialize ways & find minimum value in denoms as it can be useful in skipping a few operations
	ways, min_denom = initialize(ways, denoms)
	for i in range(1, n+1):
		res = findWays(i, denoms, ways, calculated, min_denom)
		print(res)
		ways.append(res)
	return ways.pop()

# def initialize(ways, denoms):
# 	# number of ways to make a 0 is 1. Use no coin
# 	ways.append(1)
# 	min_denoms = denoms[1]
# 	for denom in denoms:
# 		ways

def findWays(n, denoms, ways, calculated, min_denom):
	current_ways = 0
	print(n, denoms, ways)
	# min_denom improves average case. Doesn't help the worst case
	if n < min_denom:
		return 0
	for denom in denoms:
		current_denom = 0
		# reinitialize calculated for each denom calculation
		calculated = {}
		while n >= denom:
			current_denom += denom
			remaining = n - denom
			if frozenset([current_denom, remaining]) not in calculated:
				current_ways += ways[current_denom] * ways[remaining]
				calculated.add(frozenset([current_denom, remaining]))
			n = remaining
	return current_ways
	