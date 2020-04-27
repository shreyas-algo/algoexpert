# Important learnings / observations:
# 1. mid can directly be calculated if you know start_index & length. You don't really need to know the end (eases calculation in current problem)
# 2. length always changes to length / 2
# These 2 observations really help visualize the problem and make calculations easier. As now you only need to worry about proper mid indexing when the start is at an offset

# Major Fix:
# - everytime start changes, you need to find the correct start so that the array is sorted

def shiftedBinarySearch(array, target):
    result = -1
    start = findShiftIndex(array)
    # keep track of the sorted start in a variable
    current_start = start
    print("Start: {}".format(start))
    arr_len = len(array)
    curr_len = arr_len
    end = start - 1
    count = 0
    if start == 0:
        end = arr_len - 1
    # keep searching unless there are elements in the search space
    while curr_len > 0:
        # notice through an example -- mid indexing is always based on start
        if start != current_start:
            array = findSlicedArray(array)
            start = findShiftIndex(array)
            current_start = start
        mid = (start + int(curr_len/2))%arr_len
        # print("Current length: {}".format(curr_len))
        # print("checking {}: {}".format(mid, array[mid]))
        # print("*********")
        if array[mid] == target:
            return mid
        elif array[mid] > target:   # check left
            # not really requied but kept for completeness. mid calculation only done by start and length
            end = mid - 1
        else:
            start = mid + 1         # check right
            # print("Right. & new start: {}".format(start))
        curr_len = int(curr_len/2)
        count += 1
    return result

# find index where origin has shifted to. it'll basically be a dip
# todo: add logic to handle equality?
def findShiftIndex(array):
  array_len = len(array)
  if array_len == 0: return 0
  current = array[0]
  for idx in range(1, array_len):
    if array[idx] < current:
        # shift spotted
        return idx
    current = array[idx]
  return 0

def findSlicedArray(array):
    # todo: add logic to return sliced array based on start, end
    return array

# print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33))  # 8
# print(shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 0, 1, 21], 33))  # 0
# print(shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 0, 1, 21], 0))  # 7
# print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 61))  # 1 
# print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 610))  # -1 
# print(shiftedBinarySearch([0, 1, 21, 33, 45, 65, 99], 99))  # 6
# print(shiftedBinarySearch([5, 23, 111, 1], 111))  # 2 -> my ans: -1 -- because shift of origin causes bin search logic to break

# Issue: print(v1ShiftedBinarySearch([5, 23, 111, 1], 111))  # 2 -> my ans: -1 -- because shift of origin causes bin search logic to break
def v1ShiftedBinarySearch(array, target):
    result = -1
    start = v1findShiftIndex(array)
    print("Start: {}".format(start))
    arr_len = len(array)
    curr_len = arr_len
    end = start - 1
    count = 0
    if start == 0:
        end = arr_len - 1
    # keep searching unless there are elements in the search space
    while curr_len > 0:
        # notice through an example -- mid indexing is always based on start
        mid = (start + int(curr_len/2))%arr_len
        # print("Current length: {}".format(curr_len))
        # print("checking {}: {}".format(mid, array[mid]))
        # print("*********")
        if array[mid] == target:
            return mid
        elif array[mid] > target:   # check left
            # not really requied but kept for completeness. mid calculation only done by start and length
            end = mid - 1
        else:
            start = mid + 1         # check right
            # print("Right. & new start: {}".format(start))
        curr_len = int(curr_len/2)
        count += 1
    return result

def v1findShiftIndex(array):
  array_len = len(array)
  if array_len == 0: return 0
  current = array[0]
  for idx in range(1, array_len):
    if array[idx] < current:
        # shift spotted
        return idx
    current = array[idx]
  return 0

# print(v1ShiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33))  # 8
# print(v1ShiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 0, 1, 21], 33))  # 0
# print(v1ShiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 0, 1, 21], 0))  # 7
# print(v1ShiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 61))  # 1 
# print(v1ShiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 610))  # -1 
# print(v1ShiftedBinarySearch([0, 1, 21, 33, 45, 65, 99], 99))  # 6
# print(v1ShiftedBinarySearch([5, 23, 111, 1], 111))  # 2 -> my ans: -1 -- because shift of origin causes bin search logic to break


# with all comments and logic
def oldShiftedBinarySearch(array, target):
    result = -1
    start = findShiftIndex(array)
    arr_len = len(array)
    curr_len = arr_len
    end = arr_len - 1
    count = 0
    if start == 0:
        end = start - 1
    # keep searching unless there are elements in the search space
    while curr_len > 0:
        # notice through an example -- mid indexing is always based on start
        mid = (start + int(curr_len/2))%arr_len
        # print("Current length: {}".format(curr_len))
        # print("checking {}: {}".format(mid, array[mid]))
        if array[mid] == target:
            return mid
        elif array[mid] > target:   # check left
            end = mid - 1
        else:
            start = mid + 1         # check right
            # print("Right. & new start: {}".format(start))
        
        # NOT REQUIRED! curr_len will always change to curr_len/2 in binary search
        # if start <= end:
        #     curr_len = end - start + 1
        # else:
        #     curr_len = ((end + arr_len) - start) + 1
        # print("?> Count: {}".format(count))
        curr_len = int(curr_len/2)
        count += 1
    return result