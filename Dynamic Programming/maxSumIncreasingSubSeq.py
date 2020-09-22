# Approach:
# Analysis:

# Learning:
# 1. keys() gives an iterator. So if you change a dictionary while iterating it, create a copy of the keys. either list(dict.keys) or simply `for item in list(dict)` cz dict iteration is anyway on keys

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
		for leading_num in list(result):
			if array[i] > leading_num:
				placed = True
				result[array[i]] = result.pop(leading_num)
				result[array[i]]['sum'] += array[i]
				result[array[i]]['values'].append(array[i])
				
				# update max_sum if a greater sum created
				if result[array[i]]['sum'] > max_sum:
					max_sum = result[array[i]]['sum']
					max_sum_key = array[i]
					
		if not placed:
			result[array[i]] = {'sum': array[i], 'values': [array[i]]}
	return [max_sum, result[max_sum_key]['values']]
