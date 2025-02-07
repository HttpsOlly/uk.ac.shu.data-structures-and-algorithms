from distance_ok import distance_OK

def aggressive_cows_binary_search(stall_position, cow_count):

    # order stall positions into ascending numerical order (side effect: modifies original)
    stall_position.sort()

    # total number of stalls available for assignment
    stall_count = 0

    # iterate for each possible distance from 1 to the maximum distance
    low = 1
    high = stall_position[-1] - stall_position[0]

    while low <= high:
    # [alternatively] for _ in range(low, high + 1):

        # take mid-point as the distance 'd'
        d = (low + high) // 2

        if distance_OK(stall_position, d, cow_count):

            # tally the largest distance where the arrangement is possible
            stall_count = d

            low = d + 1
        else:
            high = d - 1

    return stall_count

