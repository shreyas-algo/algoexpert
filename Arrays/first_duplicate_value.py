def firstDuplicateValue(array):
    record = set()
    for i in range(len(array)):
        if array[i] in record:
            return array[i]
        record.add(array[i])
    return -1