def minNumberOfCoinsForChange(n, denoms):
	# sort the list of denominators in descending order
    denoms.sort(reverse=True)
	coins = 0
	while n >=0:
		denom = largestPossibleDivisor(denoms, n)
		if denom is not None:
			units = int(n/denom)
			coins += units
			n = n - (denom*units)
		else:
			break
	# if n fully divided
	if n == 0:
		return coins
	else:
		return -1

def largestPossibleDivisor(array, target):
  length = len(array)
  lo = 0
  hi = length - 1
  largestPossibleDivisor = None
  while lo <= hi:
    mid = int((lo+hi)/2)
    if target == array[mid]:
      return array[mid]
    elif target > array[mid]:
      # go left as array is sorted in descending order
      # whenever you find target > array[mid] (i.e whenever you go left) update largestPossibleDivisor
      largestPossibleDivisor = array[mid]
      hi = mid -1
    else:
      # keep going right as array is sorted in descending order
      lo = mid + 1
  return largestPossibleDivisor