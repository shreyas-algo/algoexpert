def sunsetViews(buildings, direction):
    max_height = 0
    result = []
    if direction == "EAST":
        # reverse traverse
        for i in range(len(buildings)-1, -1, -1):
            if buildings[i] > max_height:
                result.append(i)
                max_height = buildings[i]
        return result[::-1]
    else:
        for i in range(len(buildings)):
            if buildings[i] > max_height:
                result.append(i)
                max_height = buildings[i]
        return result