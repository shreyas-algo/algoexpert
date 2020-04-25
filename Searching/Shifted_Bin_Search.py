def shiftedBinarySearch(array, target):
    result = -1
    start = findShiftIndex(array)
    arr_len = len(array)
    curr_len = arr_len
    end = arr_len - 1
    # count = 0
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
        
        if start <= end:
            curr_len = end - start + 1
        else:
            curr_len = ((end + arr_len) - start) + 1
        # print("?> Count: {}".format(count))
        # count += 1
    return result

def findShiftIndex(array):
  # TODO: create logic to find shift point
  return 5

print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33))
print(shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 0, 1, 21], 33))