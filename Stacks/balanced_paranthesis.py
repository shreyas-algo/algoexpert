# Approach: For every opening bracket, keep pushing in a stack. For every closinb bracket, pop from stack and check it's matching from the last opened bracket. For a non-bracket character continue. If by the end of the routine the stack is empty, you have a balanced string
# Analysis: O(N)

# Learning: 
# a) Read the question. Don't assume! The question mentioned optional characters also which we did not take into account
# b) Do not shy away from dry run. It's a good practice. You'll catch silly mistakes. Keep 10-15 minutes. Take a deep breath and do it dilligently. Only then run your code. It shows standard practice.
# c) list has no push method! Use append()
# d) `if not list` & `if list` can be used to check if the list is empty and non-empty respectively
def balancedBrackets(string):
    opened_stack = []
	barcket_complement = { ']': '[', '}': '{', ')': '(' } 
	opening = {'{', '[', '('}
	closing = {'}', ']', ')'}
	for incoming_bracket in string:
		if incoming_bracket in opening:
			opened_stack.append(incoming_bracket)
		elif incoming_bracket in closing:
			# assuming that the string is only made up of valid characters
			if opened_stack:
				last_opened = opened_stack.pop()
				if last_opened != barcket_complement[incoming_bracket]:
					return False
			else:
				# closing bracket came before any opening bracket
				return False
		else:
			# allow optional characters
			continue
	# if the stack is empty in the end, everything worked out
    if not opened_stack:
		return True
	return False
