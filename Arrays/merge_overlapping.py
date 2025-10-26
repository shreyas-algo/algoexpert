def mergeOverlappingIntervals(intervals):
    result = []
    if len(intervals) == 0:
        return [[]]

    # sort intervals
    intervals = sorted(intervals, key=lambda interval: interval[0])
    
    result.append(intervals[0])
    result_len = 1

    for i in range(1, len(intervals)):
        # look back at previous entry in result and update values if continuous interval found
        prev_start, prev_end = result[result_len - 1]
        start, end = intervals[i]
        # insert right away if not continuous
        if start > prev_end:
            result.append([start,end])
            result_len += 1
        # update previous end if the new interval expands the previous range
        elif end > prev_end:
            result[result_len - 1][1] = end
            
            
    return result
