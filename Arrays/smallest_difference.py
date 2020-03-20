# Approach: Sort second array and for every element in first array, do a binary search for it in second array. Keep track of the min_difference value and return in the end
# Analysis: O(n log m) {n binary searches} + O(m log m) {sorting second array} 
def smallestDifference(arrayOne, arrayTwo):
    # sort arrays
    # arrayOne.sort()
    arrayTwo.sort()
    # init
    result = []
    len1 = len(arrayOne)
    len2 = len(arrayTwo)
    if len1 > 0 and len2 > 0:
        closest_value = abs(arrayOne[0] - arrayTwo[0])
    else:
        return None
    # todo: add optimization of sorting and using smaller array as the search array
    for item in arrayOne:
        # binary search closest value to item in second array
        low = 0
        high = len2 - 1
        mid = int((low + high) / 2)
        while low <= high:
            mid = int((low + high) / 2)
            if abs(arrayTwo[mid] - item) <= closest_value:
                    closest_value = abs(arrayTwo[mid] - item)
                    result = [item, arrayTwo[mid]]
            if arrayTwo[mid] == item:
                # if numbers match, this is the smallest possible absolute difference value
                return result
            elif arrayTwo[mid] > item:
                # go left
                high = mid - 1
            else:
                # go right
                low = mid + 1
    return result

print(smallestDifference([-1, 5], [-1, 4]))