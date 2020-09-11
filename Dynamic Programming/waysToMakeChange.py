def numberOfWaysToMakeChange(n, denoms, min_denom, results={}, count=0):
	# if results not initialized (parent call), initialize it with demons: set result for each denom as 1 so that we ca return in O(1) time when the target(n) == one of t
	# also set the min_denom
    if not results:
		if len(denoms) > 0:
			min_denom = denoms[0]
		else:
			return 0
		for denom in denoms:
			if denom < min_denom:
				min_denom = denom
			results[denom] = 1
	
	# base cases
	if n < min_denom:
		return 0
	if n in results:
		return results[n]
	
	for denom in denoms:
		while n  >= denom:
            pass
            # incomplete
			# numberOfWaysToMakeChange(n, denoms, min_denom, results={}, count=0)
    return count
