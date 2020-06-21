# Approach II: Find all peak indices. For every peak, try to expand on left & right as far as the decreasing slope satisfies. Return calculated peak_length
# Analysis: O(2N) ~ O(N) - notice that no two peak expansions will intersect for more than 1 point - because right branch of a peak can't be the left branch of another peak. strictly increasing and strictly decreasing are mutually exclusive. So total iteration for expansion's length check will go around ~N items
# O(N) space due to peaks array

# Notice: that an improvement is possible here which is not storing the peaks array but doing the branch length calculation whenever you find a peak. (AlgoExpert) Can add that update here

# Learning: Try different approaches when one becomes too difficult to manage.
def longestPeak(array):
    arr_len = len(array)
    max_peak_length = 0
    # need at least 3 integers to make a peak: see problem description
    if arr_len < 3:
        return 0

    peaks = identifyPeaks(array, arr_len)
    for p_idx in peaks:
        left = getLeftExpansion(array, p_idx)
        right = getRightExpansion(array, p_idx, arr_len)
        peak_length = left + right + 1	# +1 for the peak itself
        max_peak_length = max(peak_length, max_peak_length)
        
    return max_peak_length

    def identifyPeaks(array, arr_len):
        peaks = []
        for idx in range(1, arr_len-1):
            if array[idx] > array[idx-1] and array[idx] > array[idx+1]:
                peaks.append(idx)
        return peaks

    def getLeftExpansion(array, p_idx):
        idx = p_idx-1	# initialized with p_idx-1 because a peak will definitely be larger than the immediate left. Definition of identifyPeaks
        left_length = 1
        while idx > 0:
            if array[idx] > array[idx-1]:
                left_length += 1
                idx -= 1
            else:
                break
        return left_length

def getRightExpansion(array, p_idx, arr_len):
	idx = p_idx+1	# initialized with p_idx+1 because a peak will definitely be larger than the immediate right. Definition of identifyPeaks
	right_length = 1
	while idx < arr_len-1:
		if array[idx] > array[idx+1]:
			right_length += 1
			idx += 1
		else:
			break
	return right_length


# Approach: Update peak_found when inc -> dec (dip). Update max_peak_length when non-inc -> inc (bottom-rise). Keep updating track_length or peak_length for every element except for when current_track is flat (flats are discared from peak length)
# Analysis: O(N) time, O(1) space

def longestPeak(array):
    arr_len = len(array)
    # need at least 3 integers to make a peak: see problem description
    if arr_len < 3:
        return 0
    # init
    peak_length = 2
    max_peak_length = 0
    peak_found = False
    max_updated = False
    trajectory = getTrajectory(array[0], array[1])
    for idx in range(1, arr_len-1):
        current_track = getTrajectory(array[idx], array[idx+1])
        if current_track != "flat":
            peak_length += 1
        if trajectory == "inc" and current_track == "dec":
            peak_found = True
        if trajectory != "inc" and current_track == "inc":
            # beacuse this is bottom-rise which means current element was not a non-decreasing right (cannot be a part of the current peak_length) but added on line 68 (to keep code consistent). Thus, discard here
            peak_length -= 1
            if peak_found:
                if peak_length > max_peak_length:
                    max_peak_length = peak_length
                    max_updated = True
            peak_length = 2
            peak_found = False
        trajectory = current_track
        
    if peak_found and not max_updated:
        # For case when bottom dip switch never happened. no transfer from dec -> inc (basis for max calculation)
        return max(peak_length, max_peak_length)
    return max_peak_length

def getTrajectory(predecessor, successor):
	if successor > predecessor:
		return "inc"
	elif predecessor > successor:
		return "dec"
	else:
		return "flat"