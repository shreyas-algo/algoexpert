# Approach: Create a suffix trie of all the characters in the sentence bigString. Run contains on every smallWord
# Analysis: 
# Creation: O(n*n) time & O(n) space where n is the length of the words in the bigString
# Contains: O(mn) time (n - length of smallStrings, m - length of every word in smallStrings) & O(1) space

# Learning:
# 1. Suffix tries are great for string comparison
# 2. Discuss the meaning of "contains" with your interviewer - does it mean exact word or substring is okay. what about spaces - eg is " am " contained in "I am passionate!". How about "I a"?

def multiStringSearch(bigString, smallStrings):
    word_trie = WordTrie(bigString)
    print(word_trie.root)
    result = []
    for string in smallStrings:
      result.append(word_trie.contains(string))
    return result
      

class WordTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateWordTrieFrom(string)

    def populateWordTrieFrom(self, string):
        n = len(s)
        result = []
        for i in range(n): 
          temp="" 
          current_dict = self.root
          for j in range(i,n): 
              temp+=s[j]
              if s[j] not in current_dict:
                # if dictionary for a character doesn't exist, create it
                current_dict[s[j]] = {}
          current_dict = current_dict[s[j]]
          # add * at the end of a suffix
          current_dict[self.endSymbol] = True

    def contains(self, string):
        current_dict = self.root
        for char in string:
            if char not in current_dict:
                return False
            current_dict = current_dict[char]
        # Correct cz half words also considered right
        # if self.endSymbol in current_dict:
        #     return True
        return True
