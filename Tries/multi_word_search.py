# Question (alteration of algoexpert question): Find if any word from given array of smallStrings appears EXACTLY in the given bigString

# Approach: Create a trie of all the words in the sentence bigString (split by space). Run contains on every smallWord
# Analysis: Creation: O(m) time where m is the length of the longest word & O(n) space where n is the length of the bigString

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
        for word in string.split(" "):
          # get back to root for every word
          current_dict = self.root
          for char in word:
            if char not in current_dict:
              # if dictionary for a character doesn't exist, create it
              current_dict[char] = {}
            current_dict = current_dict[char]
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
        return True
