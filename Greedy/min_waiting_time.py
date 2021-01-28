# TODO: watch video
# Approach: sort the array in increasing order (for min waiting time). Keep calculating wait_time as you move along the array and also the wait_time_sum. 
# Analysis: O(nlogn) & O(1) space

def minimumWaitingTime(queries):
	queries.sort()
    arr_len = len(queries)
	wait_time = 0
	wait_time_sum = 0
	for i in range(1, arr_len):
        # wait_time at position i
        wait_time += queries[i-1]
        # calculate wait_time_sum on the fly
        wait_time_sum += wait_time
        # print(a[i], wait_time, wait_time_sum)
    return wait_time_sum