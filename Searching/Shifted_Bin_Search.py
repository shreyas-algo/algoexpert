def shiftedBinarySearch(array, target):
    result = -1
    start = findShiftIndex(array)
    arr_len = len(array)
    curr_len = arr_len
    end = arr_len - 1
    if start == 0:
        end = start - 1
    # keep searching unless there are elements in the search space
    while curr_len > 0:
        # notice through an example
        mid = (start + int(len/2))%curr_len
        print("checking {}: {}".format(mid, array[mid]))
        if array[mid] == target:
            return mid
        elif array[mid] > target:   # check left
            end = mid - 1
        else:
            start = mid + 1         # check right
        # todo: add code similar to bin search. Just indexed out of start_index. Understand that you don't need to have the whole array everytime. All you need is: mid, length, start_index (Using these you can always )
    return result

def findShiftIndex(array):
  # TODO: create logic to find shift point
  return 5

shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45])