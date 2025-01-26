def nonConstructibleChange(coins):
    running_sum = 0
    for coin in sorted(coins):
        if running_sum < coin and coin != running_sum + 1:
            break
        running_sum += coin
    return running_sum + 1