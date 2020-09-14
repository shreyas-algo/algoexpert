# Approach: Greedy approach. Sort denoms in descending order. Starting from the largest denom start subtracting the number and collecting coins value. If at the end n is zero, return coins (completely denominated) else return -1
# Complexity: O(dlogd){sorting} + O(log n - base min_d) {Roughly: while loop} where d: number of denominations, min_d: smallest denominations

# Good attempt.
# But incorrect Solution. Works for 12/15 cases on Algoexpert
# Only works for certain type of denomination combinations (actual currency which is complementary eg Dollar, Rupee note denomnations)
# greedy doesn't work for following cases:
# {"n": 9, "denoms": [3, 5]}  # Op: -1 --- Expected: 3 {3,3}
# {"n": 135, "denoms": [39, 45, 130, 40, 4, 1, 60, 75]} # Op: 3 --- Expected: 2 {75,60}
# {"n": 10, "denoms": [1, 3, 4]}  # Op: 4 --- Expected: 3 {4,3,3}

# Note: largestPossibleDivisor() may not be even required. It was useful if we were doing it for all denoms but it turns out that's also a greedy approach and it does help some cases but doesn't solve all cases

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

# O(logd) 
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