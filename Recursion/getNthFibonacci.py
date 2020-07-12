# Approach: Iterative
# Analysis: O(N) time & O(1) space

def getNthFib(n):
    first = 0
    second = 1
    if n == 1: return first
    if n == 2: return second
    count = 2
    while count != n:
        fib = first + second
        first = second
        second = fib
        count += 1
    return fib


# Approach II: Memoize (store) result everytime you calculate a value and use the value when another call for same value made
# Analysis: O(N) time & O(N) space

# Learning: Initially kept "memo" in the getNthFib() call which didn't really help

memo = {}
def getNthFib(n):
    if n == 1: return 0
    if n == 2: return 1
    if n in memo:
        return memo[n]
    memo[n] = getNthFib(n-1) + getNthFib(n-2)
    return memo[n]



# Approach I: Simple recursion without using memoization
# Analysis: wasted space & time due to duplicate calls. 
# O(2^N) time & O(N) space (recursion call stack)
def getNthFib(n):
    if n == 1: return 0
    if n == 2: return 1
    return getNthFib(n-1) + getNthFib(n-2) 