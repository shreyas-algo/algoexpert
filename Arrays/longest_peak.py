def longestPeak(array):
    arr_len = len(array)
    peak_length = 2
    # peak_height = 0
    max_peak_length = 0
    peak_found = False
    max_updated = False
    # need at least 3 integers to make a peak: see problem description
    if arr_len < 3:
        return 0
    trajectory = getTrajectory(array[0], array[1])
    for idx in range(1, arr_len-1):
        current_track = getTrajectory(array[idx], array[idx+1])
        if current_track != "flat":
            peak_length += 1
        print(idx, trajectory, current_track)
        # if trajectory == "inc" and current_track == "inc":
            # peak_length += 1
        if trajectory == "inc" and current_track == "dec":
            # peak_length += 1
            peak_found = True
        if trajectory != "inc" and current_track == "inc":
            # to count length properly?
            peak_length -= 1
            if peak_found:
                if peak_length > max_peak_length:
                    max_peak_length = peak_length
                    max_updated = True
                    print(max_peak_length, idx, array[idx])
            peak_length = 2
            peak_found = False
        trajectory = current_track
        
    if peak_found and not max_updated:
        # update max peak again. For case when bottom dip never happened
        return max(peak_length, max_peak_length)
    return max_peak_length

def getTrajectory(predecessor, successor):
	if successor > predecessor:
		return "inc"
	elif predecessor > successor:
		return "dec"
	else:
		return "flat"