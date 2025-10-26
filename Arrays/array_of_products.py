def arrayOfProducts(array):
    result = []
    prod = 1
    count = 0
    # find product of all numbers
    for i in range(len(array)):
        if array[i] != 0:
            prod *= array[i]
        else:
            count += 1
    # if there are zeroes in the array
    if count > 0:
        if count == 1:
            return [0 if array[i] != 0 else prod for i in range(len(array))]
        return [0 for i in range(len(array))]

    return [prod / array[i] for i in range(len(array))]
    
        
        
