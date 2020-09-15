# Test following:
# {"n": 10, "denoms": [3, 4]}  # Expected: 3 {4,3,3}

def minNumberOfCoinsForChange(n, denoms):
    # create a ways array equal to len(n) and initialize all by -1 except 0. Coins to make 0 is 0 always
	ways = []
	ways.append(0)
	for i in range(1,n+1):
		ways.append(-1)
	
	for denom in denoms:
		for num in range(n+1):
			# set current. current represents a possible answer using current denom
			current = -1
			# divisible
			if denom <= num:
				# current denom can make a solution
				if ways[num-denom] != -1:
					current = 1 + ways[num-denom]
				# if there was no previous solution, accept this
				if ways[num] == -1:
					ways[num] = current
				# if there was a previous solution, accept minimum
				else:
					ways[num] = min(ways[num], current)
	print(ways)
    return ways[n]
