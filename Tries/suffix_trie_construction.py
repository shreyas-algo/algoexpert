# Approach: Look at conceptual overview. Simply followed definition of Suffix Trie
# Construction: Create double loop to go over the suffixes in the described fashion. Assign current_dict back to root on every inner loop. Initialize current_dict[character] = {} or get existing current_dict[character] for every character depending on whether it exists or not. In the end of the inner loop, add * in the end
# Contains: Until there are characters in the string, check that the current_dict can follow same character starting from root. If at any point it doesn't, return False. If all characters passed through, the current_dict should have a * for it to be a suffix

# Analysis: 
# Construction: O(n*n) space & O(n*n) time
# Contains: O(m) time (where m is the length of the target string) & O(1) space

# Learning: 
# 1. If you understand the concept well, you will code well. Understand the question super well. Draw it out
# 2. Then while coding, keep the drawing / conceptual overview / sample input/output in front of you for ease of visualizing test cases

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        length = len(string)
		for i in range(length):
			# get back to root for every suffix start
			current_dict = self.root
			for j in range(i,length):
				if string[j] not in current_dict:
					# if dictionary for a character doesn't exist, create it
					current_dict[string[j]] = {}
				current_dict = current_dict[string[j]]
			# add * at the end of a suffix
			current_dict[self.endSymbol] = True

    def contains(self, string):
        current_dict = self.root
        for char in string:
            if char not in current_dict:
                return False
            current_dict = current_dict[char]
        if self.endSymbol in current_dict:
            return True
        return False

