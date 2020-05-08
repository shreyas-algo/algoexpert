# Approach: Keep 2 pointers. one init from start, another from end.
# case: when start == end: retain current_length as longest. i+1, end-1
# case: when start != end: (decide which side has a possible palindrome)
# if start == end - 1: end -= 1
# if start+1 == end: start += 1 
# move both start & end if neither 
def longestPalindromicSubstring(string):
    max_length = len(string)
    palindromeFound = False
    start = 0
    end = max_length - 1
    while start < end:
        if string[start] == string[end]:
            if not palindromeFound:
                palindromeFound = True
                max_length = end - start + 1
            start += 1
            end -= 1
        else:
            palindromeFound = False
            max_length = 1
            if string[start+1] == string[end]:
                start += 1
            elif string[start] == string[end-1]:
                end -= 1
            else:
                start += 1
                end -= 1
    return max_length
