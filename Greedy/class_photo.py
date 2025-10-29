def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    # assume blues are taller
    backRow = blueShirtHeights
    frontRow = redShirtHeights
    # return on equality
    if redShirtHeights[0] == blueShirtHeights[0]:
        return False
    if redShirtHeights[0] > blueShirtHeights[0]:
        backRow = redShirtHeights
        frontRow = blueShirtHeights

    # ensure all in back row are strictly taller
    for idx in range(1, len(backRow)):
        if backRow[idx] <= frontRow[idx]:
            return False
        
    return True
