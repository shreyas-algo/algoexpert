# Approach:  
# 1. create a key for all words that represents how many times each character has shown up in alphabetic order eg saasd will be `a2d1s2`
# 2. go through every word and maintain a doctionary mapping keys to all assicated anagram strings
# 3. Finally use the dictionary to return list of groups -- list(dict.values())

# Complexity Analysis:
# List length: N, Word length: k
# Overall: O(N * k log k) ~ O(N) if number of words in the language, k considered constant and not comparable to the list length

# Learning: append() returns None and not the resulting new array. Ref: Line 20

def groupAnagrams(words):
    anagram_dict = {}
    # O(N)
    for word in words:
        # O(N * k)
        anagram_key = getKeyForWord(word) # O(k)
        # if key exists, return existing array, otherwise return blank array []
        existing = anagram_dict.get(anagram_key, []) 
        existing.append(word)
        anagram_dict[anagram_key] = existing
    return list(anagram_dict.values())

# Overall: O(k)
def getKeyForWord(word):
	key_dict = {}
	# create character count dictionary
	# O(k)
	for char in word:
		char_count = key_dict.get(char, 0)
		key_dict[char] = char_count + 1
	# create the key
	key = []
	# O(k log k) -> O(number of alphabets in the language) -> O(26 log 26) (if only english) -> O(1) or O(m log m) where m is the number of alphabets allowed in the language. Thus the time taken will not grow based on length of list or length of word
    # Important: can be futher optimized to O(k) by creating an init dictionary for ascii which itself is sorted
    # But wait think about it k in this case will be maximum 26 (for alphabets)
    # So it boils down to constant time -> because k = 26 (constant). The word will atmost have all letters of the english alphabet. Hence, this optimization is not really required here. But can be a great discussion in an interview
	for k in sorted(key_dict.keys()):
		key.append(k + str(key_dict[k]))
	return "".join(key)

#########################################################################

# Approach II: Idea: sort characters in every word. Then sort the list itself to group anagrams but create either a auxillary array or object out of the word list to retain the original word. Discussed in algoexpert
# Not as optimized and unnecessarily complicated
# Important Learning: If you create a static class variable, it will be shared by all objects of solution so always reinstantiate it accordingly (Line 63)
class WordObject:    
  # class variable to store all word objects
  words = [] 

  # default constructor - added for completeness. Not required until you want to initialize some instance parameter as default constructor is inherently defined for you. Comment this and test. it will work
  def __init__(self):
    # instance variables
    self.value = ""
    self.index = 0

  # can be outside the class - think
  def create_objects_from_list(self, arr_list):
    for index,value in enumerate(arr_list):
      # deafault constructor usage
      obj = WordObject()
      # important: beacause we want to use class variable and when the solution will be called for different test cases, the same class variable will keep getting used. So always reinstantiate it to [] on every call
      obj.words = []
      obj.value = value
      obj.index = index
      self.words.append(obj)
    return self.words

def groupAnagrams(words):
    sorted_chars = list(map(lambda word: ''.join(sorted(word)), words))
    obj = WordObject()
    word_list = obj.create_objects_from_list(sorted_chars)
    word_list.sort(key=lambda x: x.value)

    current = ""
    idx = -1
    result = []
    for obj in word_list:
      print(obj.index, obj.value, type(obj))
      if obj.value != current:
        idx += 1
        current = obj.value
        result.append([words[obj.index]])
      else:
        result[idx].append(words[obj.index])

    return result

groupAnagrams(["race", "blink", "oy", "yo", "linkb", "care"])

		
				
			

		
				
			

		
				
			
