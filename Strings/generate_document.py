def generateDocument(characters, document):
    if document == "":
        return True

    # map characters
    d = {}
    for char in characters:
        d[char] = d.setdefault(char, 0) + 1

    # create target dict 
    target_dict = {}
    for char in document:
        if char in d:
            target_dict[char] = target_dict.setdefault(char, 0) + 1
        else:
            return False

    # see if document can be generated
    for char in target_dict:
        if d[char] < target_dict[char]:
            return False
            
    return True
