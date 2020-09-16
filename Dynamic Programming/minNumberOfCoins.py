# Approach: Create a ways array that keeps track of min coins for creating amount 0-n starting with one denom at a time. (Notice that coins to create 0 is 0 (base case)). Whenever a denom can successfully create a number i (current_solution = 1 + ways[i-denom]) (which is != -1), check against existing ways[i] and update result as min(ways[i], current_solution)
# Complexity: 
# Time: O(nd) where n is the amount value and d is the number of denominations
# Space: O(n) space where n is the amount value

# Learning:
# A greedy approach to start from max denom and keep dividing doesn't work here because eg 10 can be made by {4,3,3} whereas if you go by "keep dividing by max until possible" logic, you won't even get an answer. Greedy only works for certain type of denominations

# Test following to verify your approach:
# {"n": 10, "denoms": [3, 4]}  # Expected: 3 {4,3,3}  === Reteuns 3. All Ok!

# TODO: Watch video
# To understand, draw on paper for {"n": 10, "denoms": [3, 4]} & {"n": 6, "denoms": [1, 3, 4]}

def minNumberOfCoinsForChange(n, denoms):
    # create a ways array equal to len(n) and initialize all by -1 except 0. Coins to make 0 is 0 always
	ways = []
    # ways[0] = 0. 0 coins can be used to create 0
	ways.append(0)
	for i in range(1,n+1):
		ways.append(-1)
	
    # add one denom at a time to the mix
	for denom in denoms:
		for num in range(n+1):
			# initialize current. current represents a possible answer using current denom
			current = -1
			# if divisible
			if denom <= num:
				# if current denom can make a solution
				if ways[num-denom] != -1:
					current = 1 + ways[num-denom]
					# if there was no previous solution, accept solution with this denom
					if ways[num] == -1:
						ways[num] = current
					# if there was a previous solution, accept minimum
					else:
						ways[num] = min(ways[num], current)
    return ways[n]

