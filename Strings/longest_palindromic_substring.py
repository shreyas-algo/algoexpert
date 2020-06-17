# Approach II: check maxPalindrome for every index as fixed start index. Overall max wins.
# O(N*N)
# All this done to avoid complexity of O(N*N*N) which would be the case if we did palindrome check for every start index to every possible length
def longestPalindromicSubstring(string):
	string_len = len(string)
	# to keep track of current palindromic substring end. Start: start
	palEndIdx = 0
	# to keep track of overall max length
	current_palindrome_length = 1
	max_palindrome_length = 1
	# to keep track of overall max result indices
	resultStartIdx = 0
	resultEndIdx = 0
	for start, value in enumerate(string):
		palindromeFound = False
		# curr_start & end to iterate through the string (all possible solutions starting at start) and check palindromic condition
		curr_start = start
		end = string_len - 1
		while curr_start < end:
			if string[curr_start] == string[end]:
				if not palindromeFound:
					# start expecting palindrome. It will be overridden if palindrome not found
					palindromeFound = True
					palEndIdx = end
				curr_start += 1
				end -= 1
			else:
				if palindromeFound:
					palindromeFound = False
					# move start back to original start
					curr_start = start
					# do not move end as it may match with `start` and create a palindrome
				else:
					end -= 1 
		
		# if after the while loop, some palindrome was found -- this is a palindrome which begins with start & ends at palEndIdx
		if palindromeFound:
			current_palindrome_length = palEndIdx - start + 1
			if current_palindrome_length > max_palindrome_length:
				max_palindrome_length = current_palindrome_length
				resultStartIdx = start
				resultEndIdx = palEndIdx
	return string[resultStartIdx: resultEndIdx+1]


# Approach I: Keep 2 pointers. one init from start, another from end.
# case: when start == end: retain current_length as longest. i+1, end-1
# case: when start != end: (decide which side has a possible palindrome)
# if start == end - 1: end -= 1
# if start+1 == end: start += 1 
# move both start & end if neither 
# Complexity: O(N) [FLAWED]

# Result: Flawed. Good attempt. But breaks for abaxyzzyxf
# Problem: Updating both indices works only when values match. When none of the values match you can't move both ahead because one of them may be a part (start or end) of a possible palindrome
def longestPalindromicSubstringOld(string):
    max_length = len(string)
    palindromeFound = False
    start = 0
    end = max_length - 1
    palStartIdx = start
    palEndIdx = end
    while start < end:
        if string[start] == string[end]:
            if not palindromeFound:
                palindromeFound = True
                max_length = end - start + 1
                palStartIdx = start
                palEndIdx = end
            start += 1
            end -= 1
        else:
            palindromeFound = False
            # depends on what we want to return when no palindrome exists. Currently considered as the single character on which it breaks
            max_length = 1
            palStartIdx = start
            palEndIdx = start
            if string[start+1] == string[end]:
                start += 1
            elif string[start] == string[end-1]:
                end -= 1
            else:
                start += 1
                end -= 1
    # return max_length
    return string[palStartIdx: palEndIdx+1]