
# Approach: Maintain a matrix (distance) of m+1*n+1 where you build the result one character at a time. Rows represent the target array one character at a time (starting from '' character) & columns represent source string chars (starting from '' character) matrix[row][col] represents lavenshtein distance from source[col] to target[row]. 
# Notice that matrix[0][0] = '' & matrix[row][0] = row for all rows & matrix[0][col] = col for all columns
# Notice that when source[col] ==  target[row] (ie both characters are same), result is same as matrix[row-1][col-1] cz you doncan just ignore the current character (as it's a no op)
# when it's unequal, it can be built from 1+min([row][col-1], [row-1][col], [row-1][col-1]) -- cz they are all the places from where [row][col] can be created (using append, delete, substitute) -- draw example matrix and see
# Analysis: O(m*n) time & O(m*n) space where m: length of str1 & n: length of str2

# TODO: Watch Algoexpert solution
# TODO: Optimize space complexity. You don't really need the whole matrix all the time. You just need one row previous

# Interview Learnings:
# 1. Good question to ask: Can the insertion / deletion only hapeen at the ends or one particular end. If yes, which end?
# BIG: 2. Try to construct a small unit case (or ask for HINT if some time spent) which encapsulates a hard case where the decision is not trivial but needs optimization or a deep logic to kick in. 
# For example, this question might seem simple at first but when you think about 
# Can say: "I have a feeling that the solution cannot be trivial (as simple as finding larger length and subtracting common elements)"
# 3. when nothing works, try to implement a brute force or a naive solution (something which might not solve all cases but some). You can say something like "let me approach this with a naive solution and we can see on what cases it will fail."

# BIG:
# Takeaway: Learn to write unit cases that will break your solution. Even when you know that your solution won't work. Write your solution. Run a success case and then try to create test cases where it will break. Once you find the case, fix it or rethink solution. 
# This displays that you can use new knowledge and make a decision whether you need to tweak your code or reconstruct it. And it is a plus point.
# Remember: It's all about a good discussion. You may not be able to solve the problem but if you can show that you can communicate well and ask questions and ask for help when needed. Write some code and write test cases to test / breka your code, you're one hell of a candidate. Don't be defensive about your knowledge or solutions. Talk them through. there's no hiding in an interview. Stay calm and work through problems. Engage the interviewer.


def levenshteinDistance(str1, str2):
	target_len = len(str2)
	source_len = len(str1)
	distance = []
    # create distance matrix and init
	for row in range(target_len+1):
		for col in range(source_len+1):
			if col == 0:
				distance.append([row])
				continue
			if row == 0:
				distance[row].append(col)
			else:
				distance[row].append(0)
	
	print(distance)
	# enumerate with counter 1
	for row, char2 in enumerate(str2, 1):
  		for col, char1 in enumerate(str1, 1):
			# print(row,col)
			if char2 == char1:
				distance[row][col] = distance[row-1][col-1]
			else:
				distance[row][col] = 1+min(distance[row-1][col-1],  distance[row][col-1],  distance[row-1][col])
	print(distance)
	return distance[target_len][source_len]
			

