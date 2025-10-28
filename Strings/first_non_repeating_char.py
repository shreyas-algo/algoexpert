def firstNonRepeatingCharacter(string):
    d = {}
    for idx, char in enumerate(string):
        if char in d:
            d[char] = (idx, d[char][1] + 1)
        else:
             # save a tuple of (where, count)
            d[char] = (idx, 1)

    # iterate over dict and return first non-repeating index
    # dictionaries are ordered fron v3.7 so doesn't need extra sorting
    for (idx, count) in d.values():
        if count == 1:
            return idx
    return -1


# "abcdcaf" -> 1 (b)
# "faadabcbbebdfe" -> 3 (d)