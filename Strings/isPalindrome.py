def isPalindrome(string):
    lo = 0
    hi = len(string) - 1
    while lo < hi:
        if string[lo] != string[hi]:
            return False
        lo += 1
        hi -= 1
    return True