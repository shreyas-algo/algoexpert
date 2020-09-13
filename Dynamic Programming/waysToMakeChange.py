#TODO: probable improvement of code if you use dictionary for ways instead of a list. where you can init the dictionary with ways[denoms] as 1

def numberOfWaysToMakeChange(n, denoms):
	# edge case
	if len(denoms) == 0:
		return 0
	# ways stores number of ways to store a value i
	ways = []
	# number of ways to make a sum of 0 is 1. Use no coins
	ways.append(1)
	# calculated keeps track of pairs for which ways have already been added
	# just declared here for saving space. re init in findWays function
	calculated = set()
	# initialize ways & find minimum value in denoms as it can be useful in skipping a few operations
	min_denom = min(denoms)
	for i in range(1, n+1):
		res = findWays(i, denoms, ways, calculated, min_denom)
		print("result:",i, res)
		ways.append(res)
	print(ways)
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
		if n == denom:
			current_ways += 1
			continue
		
		step = denom
		# TODO: find better way to reinitialize a set
		# reinitialize calculated for each denom calculation
		calculated = {''}
		while n - denom > 0:
			remaining = n - denom
			print("d",denom, remaining)
			if frozenset([denom, remaining]) not in calculated:
				current_ways += ways[denom] * ways[remaining]
				calculated.add(frozenset([denom, remaining]))

			print("----here", n, remaining)
			denom = denom + step
	return current_ways
	