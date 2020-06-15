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
        # O(N * k log k)
        anagram_key = getKeyForWord(word)
        # if key exists, return existing array, otherwise return blank array []
        existing = anagram_dict.get(anagram_key, []) 
        existing.append(word)
        anagram_dict[anagram_key] = existing
    return list(anagram_dict.values())

# Overall: O(k log k)
def getKeyForWord(word):
	key_dict = {}
	# create character count dictionary
	# O(k)
	for char in word:
		char_count = key_dict.get(char, 0)
		key_dict[char] = char_count + 1
	# create the key
	key = []
	# O(k log k)
	for k in sorted(key_dict.keys()):
		key.append(k + str(key_dict[k]))
	return "".join(key)
		
				
			

		
				
			

		
				
			
