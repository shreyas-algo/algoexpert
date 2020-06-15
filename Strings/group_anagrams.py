# Approach:  
# 1. create a key for all words that represents how many times each character has shown up in alphabetic order eg saasd will be `a2d1s2`
# 2. go through every word and maintain a doctionary mapping keys to all assicated anagram strings
# 3. Finally use the dictionary to return list of groups -- list(dict.values())

# Complexity Analysis:
# List length: N, Word length: k

# Overall: O(N * k log k)
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
		
				
			

		
				
			

		
				
			
