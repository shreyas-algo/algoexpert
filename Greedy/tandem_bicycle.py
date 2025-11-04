def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    sum = 0
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()

    for i in range(len(redShirtSpeeds)):
        sum += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return sum
