# Root approach:
# create an auxiliary indices array and sort it based on value at index i in scores
# get index one at a time from the sorted indices array (get min score at a time)
# check scores[i-1] & scores[i+1] to get neighboring rewards if any and get max(neighbors)+1 to get the next reward value
# assign in rewards array

# Approach I: Use heap to get min one by one and aply counting logic
# Approach II: Create an index array from the numbers and sort the indices array based on scores[index]
# Analysis: O(n log n) time & O(n) space

# Both techniques will be O(nlogn). I think II will need extra O(n) space due to the extra index array  
# 1. can go with II & discuss improvement of using heap as heap implementation will take time and will be another problem in itself
# 2. can also abstract heap implementaion and assume it as a library and later code it if you have time

# Learning:
# 1. Weighing two solutions and choosing the best (whichever ensures best results in an interview)
# 2. Wriritng clean solutions is always easy to debug

# TODO: watch video

# Implemented II:
def minRewards(scores):
	scores_len = len(scores)
    # init rewards array
	rewards = [0 for i in range(scores_len)]
    # init indices array
	indices = [i for i in range(scores_len)]
    # sort indices based on value in rewards[i]
	indices.sort(key=lambda x: scores[x])
	for index in indices:
		reward = getNextRewardValue(index, rewards, scores_len)
		rewards[index] = reward
    # return sum of array as the result
	return sum(rewards)
	
def getNextRewardValue(index, rewards, arr_len):
    # check array bounds & send max+1 (left bound is 0 & right bound is arr_len-1)
	left = rewards[index - 1] if index - 1 >= 0 else 0
	right = rewards[index + 1] if index + 1 < arr_len else 0
	return max(left, right) + 1
	