# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# mul = 1
# sum = 0
# def productSum(array):
# 	return findSum(array, 0, 1)

		
# def findSum(array, sum, mul):
# 	if array:
# 		item = array.pop(0)
# 		if type(item) == int:
# 			sum += item
# 			productSum(array)
# 		mul += 1
# 		return sum + findSum(item, sum, mul)
# 	return sum 


def productSum(array, sum=0, mul=1):
    if not array or type(array) == int:
		return sum
	# print(array)
	item = array.pop(0)
	if type(item) == int:
		print(item, mul, item * mul, sum)
		sum += item * mul
		return productSum(array, sum, mul)
	sum = productSum(item, sum, mul+1)
	return productSum(array, sum, mul)