# I. Approach used: Break dowmn in a problem of two-sum. For every number, create a 2_sum_target (called target in code) which you look for in the remaining array. The question basically becomes n iterations of two-sum
# Sort & sorted() used to satisfy the given condition of result array being sorted
# Time complexity: O(N*N)
# Space complexity: O(N*N) -- passed set of ~N length stored for every number
def threeNumberSum(array, targetSum):
    result = []
    length = len(array)
    array.sort()
    for idx in range(length-1):
        target = targetSum - array[idx]
        passed = set()
        for idx2 in range(idx+1, length):
            if target - array[idx2] in passed:
                result.append([array[idx], target - array[idx2], array[idx2]])
            passed.add(array[idx2])
    return sorted(result)

# II. Approach used: Sort & Sliding Window / 2 pointer
# Time complexity: O(N*N)
# Space complexity: O(1)
# Algoexpert solution. No extra space. Sliding window
def threeNumberSum(array, targetSum):
    result = []
    array.sort()
    length = len(array)
    for idx in range(length - 1):
        low = idx + 1
        high = length - 1
        target = targetSum - array[idx]
        while low < high:
            print(low, high)
            sum = array[low] + array[high]
            if sum == target:
                result.append([array[idx], array[low], array[high]])
                # when found, both indices can be changed as it is given that the array consists of unique values. So once a combination is found, it isn't possible to use one of the numbers can't be used again without the other number
                low += 1
                high -= 1
            elif sum < target:
                low += 1
            else:
                high -= 1
    return result