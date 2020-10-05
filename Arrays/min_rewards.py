# Root approach: create a rewards/counter array initialized by 0 (which will be result). get min from scores one by one and apply counting logic: for the position of the received min in the counter array, check the value of counter for adjacent positions and assign the higher_val+1 (as when coming across a number if counter array is already filled, they had a lower score than the current number)
# note: counter = rewards

# Approach I: Use heap to get min one by one and aply counting logic
# Approach II: Create an index array from the numbers and sort the 

# Both techniques will be O(nlogn). I think II will need extra O(n) space due to the extra index array  
# 1. can go with II & discuss improvement of using heap as heap implementation will take time and will be another problem in itself
# 2. can also abstract heap implementaion and assume it as a library and later code it if you have time

# Learning:
# !. Weighing two solutions and choosing the best (whichever ensures best results in an interview)

# Implemented II:
def minRewards(scores):
	scores_len = len(scores)
	rewards = [0 for i in range(scores_len)]
	indices = [i for i in range(scores_len)]
	indices.sort(key=lambda x: scores[x])
	for index in indices:
		reward = getNextRewardValue(index, rewards, scores_len)
		rewards[index] = reward
	return sum(rewards)
	
def getNextRewardValue(index, rewards, arr_len):
	left = rewards[index - 1] if index - 1 >= 0 else 0
	right = rewards[index + 1] if index + 1 < arr_len else 0
	return max(left, right) + 1
	