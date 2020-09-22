# Approach:
# Analysis:

# Learning:
# 1. keys() gives an iterator. So if you change a dictionary while iterating it, create a copy of the keys. either list(dict.keys) or simply `for item in list(dict)` cz dict iteration is anyway on keys

# Approach:
# Analysis:

# Learning:
# 1. keys() gives an iterator. So if you change a dictionary while iterating it, create a copy of the keys. either list(dict.keys) or simply `for item in list(dict)` cz dict iteration is anyway on keys

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
	result[max_sum] = {'sum': max_sum, 'values': [max_sum]}
	for i in range(1, arr_len):
		placed = False
		replace = {}
		for leading_num in sorted(list(result.keys()), reverse=True):
			# print(array[i], leading_num)
			if array[i] > leading_num:
				placed = True
				
				temp = result.pop(leading_num)
				# replace[leading_num] = deepcopy(temp)
				result[leading_num] = deepcopy(temp)
				
				result[array[i]] = temp
				result[array[i]]['sum'] += array[i]
				result[array[i]]['values'].append(array[i])
				
				# update max_sum if a greater sum created
				if result[array[i]]['sum'] > max_sum:
					max_sum = result[array[i]]['sum']
					max_sum_key = array[i]
				break
				
		# for key in replace:
		# 	print(">>",key)
		# 	result[key] = replace[key]
		
		if not placed:
			result[array[i]] = {'sum': array[i], 'values': [array[i]]}
		print(array[i],result)
		print("*******")
	return [max_sum, result[max_sum_key]['values']]

