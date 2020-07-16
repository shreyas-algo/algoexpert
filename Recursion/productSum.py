
# Learning:
# IMPORTANT:
# 0. For recursion: Always think 2 things:
# a) Base case - from where answer will be returned
# b) Reurrence relation - how do you use the same function for a smaller input / repeating pattern
# 1. SMART: Simplified problem to only returning sum of all elements of the array. which basically ensures that recursion is calling all elements properly. Then add "multiplier" related code. Solving a subset of the problem not only gives you a better idea of what's happening but it also adds loads of confidence
# [low] 2. Use if - else properly for complicated questions. (Dont be lazy. Write proper if-else) Do not use iterative assumption of - if there's a return in if, no need to wrtie else, simply write code

def productSum(array, sum=0, mul=1):
	if not array:
		return sum
	item = array.pop(0)
	if type(item) == int:
		sum += item * mul
		print(item, mul, item*mul, sum, array)
		return productSum(array, sum, mul)
	else:
		sum = productSum(item, sum, mul+1)
		return productSum(array, sum, mul)
	
	