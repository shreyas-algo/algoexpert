def shiftedBinarySearch(array, target):
  start_index = findShiftIndex(array)
  result = shiftedBinarySearchHelper(array, target, start_index)
  return result

def shiftedBinarySearchHelper(a, target, start_index):
  arr_len = len(array)
  if arr_len == 0:
    return -1
  mid = (start_index + int(arr_len/2))%arr_len
  if a[mid] == target:
    return mid
  elif a[mid] > target:
    if start_index < mid:
      shiftedBinarySearchHelper(a[start_index:mid], target, start_index)
    else:
      shiftedBinarySearchHelper(a[start_index:]+a[:mid], target, start_index)
  else:
    if end_indx > mid:
      shiftedBinarySearchHelper(a[mid+1:end_indx], target, start_index)
    else:
      shiftedBinarySearchHelper(a[mid+1:]+a[:end_indx], target, start_index)

def findShiftIndex(array):
  # TODO: create logic to find shift point
  return 5

shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45])