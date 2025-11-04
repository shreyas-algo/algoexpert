def minimumCharactersForWords(words):
    result = {}
    result_arr = []
    for word in words:
        word_dict = {}
        for char in word:
            val = word_dict.setdefault(char, 0)
            word_dict[char] = val + 1
        
        # update result if more chars needed for the word to be built
        for char, value in word_dict.items():
            if char not in result or result[char] < value:
                result[char] = value

    # create result array
    for char, count in result.items():
        while count > 0:
            result_arr.append(char)
            count -= 1

    return result_arr
