# Brute Force: for every index, go over the hops and see if items repeat
# O(N*N) time - for every item, you'll traverse the whole array in case if it's a single cycle array (True case)

# Optimization: Think about it. You dont actually need to check all indexes. if you start from 0 and reach 0 without any repetition - that means the path is a single cycle which does not repeat any index. Which means no matter where you start you will have a successful single cycle
# O(N) time & O(1) space

def hasSingleCycle(array):
    arr_len = len(array)
    curr_idx = 0
    passed = []
    count = 0
    while True:
        # if you're back to 0 and you traversed whole array elements (count check) -- then it's a single cycle input
        if curr_idx == 0 and count == arr_len:
            return True
        # if you have already traversed this index without completing the single cycle path, there is a copy visit, hence False
        if curr_idx in passed:
            return False	
        else:
        # visit next, if all good
            passed.append(curr_idx)
            curr_idx = (curr_idx + array[curr_idx]) % arr_len
        count += 1
    return True

hasSingleCycle([2, 3, 1, -4, -4, 2])
# single cycle 
# complete index(value_at_index):
# 0(2) -> 2(1) -> 3(-4) -> -1(2) -> 1(3) -> 4(-4) -> 0 :: True

