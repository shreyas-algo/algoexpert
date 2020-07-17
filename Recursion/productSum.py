# Approach I (self): keep popping element until array is non-empty. check if it's of int type, simply add to sum and call function for remaining array. If the popped element is an array, call the function first for the popped element and then for remaining array
# O(N) time & O(k) space where k is the max depth of brackets

# Actually O(N*k) time due to factorial so not as efficient but good effort getting the solution to work

# Learning:
# IMPORTANT:
# 1. Read the question correctly. Notice that it's not only depth multiplication. It's current depth multiplied by outer depth
# 2. ** Just because it is mentioned to use recursion doesn't mean you cannot use iteration at all! Notice that in Algoexpert's solution the outer part is iterative
# 3. For recursion: Always think 2 things:
# a) Base case - from where answer will be returned
# b) Reurrence relation - how do you use the same function for a smaller input / repeating pattern
# 4. SMART: Simplified problem to only returning sum of all elements of the array. which basically ensures that recursion is calling all elements properly. Then add "multiplier" related code. Solving a subset of the problem not only gives you a better idea of what's happening but it also adds loads of confidence
# [low] 2. Use if - else properly for complicated questions. (Dont be lazy. Write proper if-else) Do not use iterative assumption of - if there's a return in if, no need to wrtie else, simply write code

# Notice that as you go inside in depths, the current depth is multiplied by what's outside depth which creates a factorial like pattern. basically every element is multiplied by factorial(h) where h is the depth

import math
def productSum(array, sum=0, depth=1):
	if not array:
		return sum
	item = array.pop(0)
	if type(item) == int:
		sum += item * math.factorial(depth)
		return productSum(array, sum, depth)
	else:
		sum = productSum(item, sum, depth + 1)
		return productSum(array, sum, depth)


# Approach II: (Algoexpert) Go over array in iterative fashion, calculate sum & multiply multiplier in the end before returning. If list is encountered, iteratively call same function
# O(N) time & O(k) space where k is max depth
def productSum(array, mul=1):
	sum = 0
	for item in array:
		if type(item) is list:
			sum += productSum(item, mul+1)
		else:
			sum += item
	return sum * mul


	
	
	
	