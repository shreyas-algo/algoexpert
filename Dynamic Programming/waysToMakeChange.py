def numberOfWaysToMakeChange(n, denoms):
	# init ways . notice that ways[0] = 1. There's one way to make 0 is that you choose no coins. Init all other entries by 0
	ways = []
	ways.append(1)
	for i in range(n+1):
		ways.append(0)
	
	# code:
	for denom in denoms:
		for num in range(n+1):
			if denom <= num:
				ways[num] += ways[num-denom]
	return ways[n]
	