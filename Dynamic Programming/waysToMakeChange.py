# Approach: Maintain an arrayb of ways for all numbers 0 to n where ways[i] is the number of ways i can be made. Do one denom at a time. Keep adding to existing ways entry. Start from small numbers and you'll see that way[i] is actually dependent on ways[i-denom]
# Complexity: O(nd) time & O(n) space where n: amount passed, d: number of denminations

# To understand create the table for:
# {denom: [2,3,7], n: 12} | Output: 4

def numberOfWaysToMakeChange(n, denoms):
	# init ways . notice that ways[0] = 1. There's one way to make 0 is that you choose no coins. Init all other entries by 0
	ways = []
	ways.append(1)
	for i in range(n+1):
		ways.append(0)
	
	# core code:
	# include one denom at a time
	for denom in denoms:
		for num in range(n+1):
			# if divisible
			if denom <= num:
				# add to existing ways if the difference can be created (ie ways[0] != 0)
				ways[num] += ways[num-denom]
	return ways[n]
	