# follows 2-sum logic
def semordnilap(words):
    reversed_words = set()
    result = []
    # save complement for all words
    for word in words:
        reversed_wrod = word[::-1]
        if word in reversed_words:
            result.append([word, reversed_wrod])
        reversed_words.add(reversed_wrod)

    return result

#   "words": ["dog", "desserts", "god", "stressed"]
#   output: [["dog", "god"], ["desserts", "stressed"]]