def commonCharacters(strings):
    d = {}
    result = []
    # create a base based on first string. non-empty list given so safe to do strings[0]
    for char in strings[0]:
        # count only unique
        if char not in d:
            d[char] = 1
            
    for string in strings[1:]:
        visited = set()
        for char in string:
            if char in d and char not in visited:
                d[char] += 1
                visited.add(char)

    # check how many chars were in all strings. This can even be done in the inner loop above but this is cleaner
    target_count = len(strings)
    for char in d:
        if d[char] == target_count:
            result.append(char)
    return result
