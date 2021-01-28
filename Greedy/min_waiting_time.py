# Approach: sort the array in increasing order (for min waiting time). Keep calculating waiting time as you move along the array. 
# Note that the waiting time at a pos i will be processed[i-1]
# where processed[i-1] -> time taken to process i-1 process

# Analysis: O(nlogn) & O(1) space
def minimumWaitingTime(queries):
	queries.sort()
    arr_len = len(queries)
	processed = 0
	wait_time = 0
	for i in range(1, arr_len):
	  processed += queries[i-1]
	  wait_time += processed
    return wait_time