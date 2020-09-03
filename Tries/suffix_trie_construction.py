# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.

# Approach: Look at conceptual overview. Simply followed definition of Suffix Trie

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
        # Write your code here.
        pass
