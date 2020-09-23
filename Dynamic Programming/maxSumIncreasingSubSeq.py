# Approach:
# At each step, maximise the resultant sum if an element (leading_number) is included (go through all places where it can be a leading num) and also keep a copy of existing equaltion it appends to ie. maintain the exieitng value for leading_num also just in case it can be ude son future
# Analysis:

# Learning:
# 1. keys() gives an iterator. So if you change a dictionary while iterating it, create a copy of the keys. either list(dict.keys) or simply `for item in list(dict)` cz dict iteration is anyway on keys
# 2. copy of a dict does not create a copy of it's inner lists. To create a complete copy, use deepcopy (be cautious with this, it is time & space intensive)

# Commit History | Dev History (check old commits for details)
# 1. The code went through an iteration of whether to just sort result.keys() in descending order and add an incoming number to simply the highest leading number (break inner for loop when found) but then that solution suffers because it does not consider all possibilities. A bunch of smaller numbers adding up can overtake any large leading_num 
# 2. Also for 1. to be mitigated it was important that when a leading_num key was updated, it's original value was also restored in result 
# 3. Also, deepcopy is important as you want seoarate copies of the dicitonary against leading_num cz you want independent edits on the dictionary & the inner list

# Questions to ask | Interview:
# 1. Will negative nubers exist? - Yes
# 2. Will numbers repeat? - may need code update 

# TODO: Watch video
# TODO: Fix for negative values

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
	result[max_sum_key] = {'sum': max_sum, 'values': [max_sum]}
    # required in inner for loop to maximise resultant sum
	target_leading_num = array[0]
	for i in range(1, arr_len):
		to_be_placed = False
		max_resultant_sum = 0
		for leading_num in sorted(list(result.keys()), reverse=True):
			print(array[i], leading_num, result[leading_num])
			if array[i] > leading_num:
				print("in greater")
				to_be_placed = True
				
				possible_sum = result[leading_num]['sum'] + array[i]
				
                # save the target_leading_num for which sum can be maximised
				if possible_sum > max_resultant_sum:
					target_leading_num = leading_num
					max_resultant_sum = possible_sum
				
				# update max_sum if a greater sum created
				if possible_sum > max_sum:
					max_sum = possible_sum
					max_sum_key = array[i]
				# break
		
        # make decision on how result[array[i]] will be initialized (does it add up to something ecisting or is it a new entry)
		if not to_be_placed:
			result[array[i]] = {'sum': array[i], 'values': [array[i]]}
		else:
			print(">>>",target_leading_num)
			temp = result.pop(target_leading_num)
			# place existing dict for leading_num back in dictionary before updating it as it can be used in a future possibility
			result[target_leading_num] = deepcopy(temp)

            # update result and place an entry for the current array[i] which initializes from the dict value which was already there but whose leading_num was smaller and which could lead to the biggest possible sum
			result[array[i]] = temp
			result[array[i]]['sum'] += array[i]
			result[array[i]]['values'].append(array[i])
			print(result[array[i]])
			
		print(array[i],result)
		print("*******")
	return [max_sum, result[max_sum_key]['values']]


