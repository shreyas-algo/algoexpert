def bestSeat(seats):
    running_sum = 0
    max_sum = 0
    start_idx = None
    result = -1
    at_least_one_seat = False
    
    # find longest sequence of empty seats
    for seat_index, occupied in enumerate(seats):
        if not occupied:
            at_least_one_seat = True
            if not start_idx:
                start_idx = seat_index
                running_sum = 1
            else:
                running_sum += 1
        else:
            # when you reach a filled seat, close previous calculation
            if running_sum > max_sum:
                max_sum = running_sum
                # continuous 0s ended at the previous step
                result = int((start_idx + seat_index - 1) / 2)
            # re-initialize
            start_idx = None
            running_sum = 0

    if at_least_one_seat:
        # this will only happen in the edge case that all seats are free.
        if result == -1:
            result = int((len(seats) - 1)/ 2)

        return result
                
    return -1
