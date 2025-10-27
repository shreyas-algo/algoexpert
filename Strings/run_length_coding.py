def runLengthEncoding(string):	
    if len(string) < 1:
        return None
        
    current_char = string[0]
    current_count = 0
    result = ""
    for char in string:
        if char == current_char and current_count < 9:
            current_count += 1
        else:
            result += str(current_count) + current_char
            current_char = char
            current_count = 1

    result += str(current_count) + current_char
    return result
