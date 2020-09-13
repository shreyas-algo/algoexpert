def numberOfWaysToMakeChange(n, denoms):
	# edge case
	if len(denoms) == 0:
		return 0
	# ways stores number of ways to store a value i
	ways = []
	# number of ways to make a sum of 0 is 1. Use no coins
	ways.append(1)
	min_denom = min(denoms)
	for i in range(1, n+1):
		res = findWays(i, denoms, ways, min_denom)
		print("result:",i, res)
		ways.append(res)
	print(ways)
	return ways.pop()

def findWays(n, denoms, ways, min_denom):
	current_ways = 0
	calculated = set()
	print(n, denoms, ways)
	# min_denom improves average case. Doesn't help the worst case
	if n < min_denom:
		return 0
	for denom in denoms:
		if n == denom:
			current_ways += 1
		elif n > denom:
			remaining = n - denom
			print("d",denom, remaining)
			if frozenset([denom, remaining]) not in calculated:
				current_ways += ways[denom] * ways[remaining]
				calculated.add(frozenset([denom, remaining]))
	return current_ways
	