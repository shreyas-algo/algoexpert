# Sol 1
# Worst case: O(n^2) -- if array is all 1s but average case is better (O(n)) if the incoming array is not expected to have too many 1s
def sorted_squared_array(array):
    new_array = []
    for num in array:
        # insert all 1s in the beginning - insert is an O(n) operation
        if num == 1:
            new_array.insert(0, num)
        else:
            new_array.append(num * num)
    return sorted(new_array)

# Sol 2
# Worst case: n log n -- due to sort
def sortedSquaredArray(array):
    new_array = []
    for num in array:
        new_array.append(num * num)
    return sorted(new_array)
