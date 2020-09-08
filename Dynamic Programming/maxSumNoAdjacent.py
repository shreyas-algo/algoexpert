def maxSubsetSumNoAdjacent(array):
	# aedge cases
	arr_len = len(array)
	if arr_len == 0:
		return 0
	if arr_len == 1:
		return array[0]
	elif arr_len == 2:
		return max(array[0], array[1])
	# init
	result = []
	result.append(array[0])
	result.append(max(array[0], array[1]))
    for idx,item in enumerate(array):
		next_item = max(item+array[idx-2], array[idx-1])
		result.append(next_item)
		
	return result.pop()
