# Approach I: Create a copy array of same size (initialized with 0). Iterate through the given array and start putting the target element at back of the array one by one and start putting other elements from start
# Complexity: O(N) time & O(N) space

# Approach II: Sort so that all target element is together and then swap elements that come after the target element 
# Complexity: O(N log N) time & O(1) space

# **Approach III: 2 pointers / sliding window: Traverse thorugh the array and keep swapping other numbers with last non-target element you saw
# Complexity: O(N) time & O(1) space (Well done!)