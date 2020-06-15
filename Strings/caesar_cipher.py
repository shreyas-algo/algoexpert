def caesarCipherEncryptor(string, key):
    result = []
    # TODO: Instead of base calculation twice -- you can simply do `x % (26+base)`
    base = ord('a')
    for ch in string:
        # to wrap around 26 alphabets and to start from a -> 0. ord returns ascii which is 97 for a
        shift = ((ord(ch) - base) + key) % 26
        # change back to character shifted back to ascii
        char = chr(shift + base)
        result.append(char)
    # array & ''.join used cz str += takes O(n) time because of how strings are implemented (read more)
    return ''.join(result)
