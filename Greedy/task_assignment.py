# Approach: sort indices based on task length. Then, assign batches of tasks to the workers in alternating fashion (first by decreasing task length from max task len & then by increasing task length) so that the pair sum remains minimum
# Analysis: O(n log n)

# TODO: watch video
from collections import deque

# TODO: add solution which simply works for 2k. Will not need the "round" consideration
# can even put the round consideration in a separate function which may or may not be used

# can ignore below solution as it goes out of scope of question
# Approach Ib: Same solution as above. This is just more dynamic and doesn't expect only 2k tasks
# Dynamic: will work even if there are 3k, 4k tasks.. ALternates between max time tasks and min time tasks
def taskAssignment(k, tasks):
    task_assignemnt = []
	task_len = len(tasks)
	indices = [i for i in range(task_len)]
	# sort indices in ascending order of task size (as pop() used later)
	indices.sort(key=lambda x: tasks[x])
	indices = deque(indices)
	print("indices", indices)
	# initialize task_assignemnt
	for worker_numer in range(k):
		task_assignemnt.append([])
	
	round = 0
	for worker_numer in range(2*k):
		# as already given that tasks will be 2k, no need to add try except to pop() 		 
		if round % 2 == 0:
			task_index = indices.pop()
		else:
			task_index = indices.popleft()
		task_assignemnt[worker_numer%k].append(task_index)
        # update round when worker_numer%k is going to be updated back to 0 in next round
		if (worker_numer%k)+1 == k:
			round += 1
	print("task_assignemnt", task_assignemnt)
    return task_assignemnt
