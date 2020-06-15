# Approach:  
# 1. create a key for all words that represents how many times each character has shown up in alphabetic order eg saasd will be `a2d1s2`
# 2. go through every word and maintain a doctionary mapping keys to all assicated anagram strings
# 3. Finally use the dictionary to return list of groups -- list(dict.values())

def groupAnagrams(words):
    anagram_dict = {}
    for word in words:
        anagram_key = getKeyForWord(word)
        # if key exists, return existing array, otherwise return blank array []
        existing = anagram_dict.get(anagram_key, []) 
        existing.append(word)
        anagram_dict[anagram_key] = existing
    return list(anagram_dict.values())

def getKeyForWord(word):
	key_dict = {}
	# create character count dictionary
	for char in word:
		char_count = key_dict.get(char, 0)
		key_dict[char] = char_count + 1
	# create the key
    # TODO: Instead of `str +=`, use res_array & then ``"".join(res_array)` approach coz str+ takes O(n) time every time you add a character due to the underlying implementation (read more)
	key = ""
	for k in sorted(key_dict.keys()):
		key += k + str(key_dict[k])
	return key
		
				
			
