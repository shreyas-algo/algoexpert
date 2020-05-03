# Brute Force: for every index, go over the hops and see if items repeat
# O(N*N) time - for every item, you'll traverse the whole array in case if it's a single cycle array (True case)
def hasSingleCycle(array):
    arr_len = len(array)
    for idx, val in enumerate(array):
        curr_idx = idx
        # curr_val = array[curr_idx] 
        passed = []
        count = 0
        while True:
            if curr_idx == idx and count == arr_len:
                return True
            if curr_idx in passed:
                print(idx, curr_idx)
                return False	
            else:
                passed.append(curr_idx)
                curr_idx = (curr_idx + array[curr_idx]) % arr_len
            count += 1
    return True

# Optimization: ?
