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
			current_dict = self.root
			for j in range(i,length):
				if j not in current_dict:
					current_dict[j] = {}
				current_dict = current_dict[j]
			current_dict[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        pass
