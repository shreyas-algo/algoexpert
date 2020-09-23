# Approach:
# Analysis:

# Learning:
# 1. keys() gives an iterator. So if you change a dictionary while iterating it, create a copy of the keys. either list(dict.keys) or simply `for item in list(dict)` cz dict iteration is anyway on keys
# 2. copy of a dict does not create a copy of it's inner lists. To create a complete copy, use deepcopy (be cautious with this, it is time & space intensive)

from copy import deepcopy
def maxSumIncreasingSubsequence(array):
	# edge case
	arr_len = len(array)
	if arr_len == 0:
		return None
    # init
	result = {}
	max_sum = array[0]
	max_sum_key = array[0]
	target_leading_num = array[0]
	result[max_sum_key] = {'sum': max_sum, 'values': [max_sum]}
	for i in range(1, arr_len):
		placed = False
		replace = {} 
		max_resultant_sum = 0
		for leading_num in sorted(list(result.keys()), reverse=True):
			print(array[i], leading_num, result[leading_num])
			if array[i] > leading_num:
				print("in greater")
				placed = True
				
				possible_sum = result[leading_num]['sum'] + array[i]
				
				if possible_sum > max_resultant_sum:
					target_leading_num = leading_num
					max_resultant_sum = possible_sum
				
				# update max_sum if a greater sum created
				if possible_sum > max_sum:
					max_sum = possible_sum
					max_sum_key = array[i]
				# break
		
		if not placed:
			result[array[i]] = {'sum': array[i], 'values': [array[i]]}
		else:
			print(">>>",target_leading_num)
			temp = result.pop(target_leading_num)
			# place existing dict for leading_num back in dictionary before updating it as it can be used in a future possibility
			result[target_leading_num] = deepcopy(temp)

			result[array[i]] = temp
			result[array[i]]['sum'] += array[i]
			result[array[i]]['values'].append(array[i])
			print(result[array[i]])
			
		print(array[i],result)
		print("*******")
	return [max_sum, result[max_sum_key]['values']]


