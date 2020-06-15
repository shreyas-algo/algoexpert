# Approach: 2 pointer. start & end and keep checking until either one mismatches (not a palindrome) or lo==hi (is a palindrome)

# the video explanantion on algoexpert is pretty cool. go watch it
# it also discusses tail recursion which is great
# IMP: when you're using recursion always mention that the solution is going to use extra memory due to the call stack 
# and then maybe mention tail recursion optimization in code (last line should be recursive call) and also by compiler (some compliers optimize even when recursive call is not last statement)

# solution: self
def isPalindrome(string):
    lo = 0
    hi = len(string) - 1
    while lo < hi:
        if string[lo] != string[hi]:
            return False
        lo += 1
        hi -= 1
    return True