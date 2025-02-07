from distance_ok import distance_OK

def aggressive_cows_linear_search(stall_position, cow_count):

    # order stall positions into ascending numerical order (side effect: modifies original)
    stall_position.sort()

    # total number of stalls available for assignment
    stall_count = 0

    # iterate for each possible distance from 1 to the maximum distance
    for d in range(1, max(stall_position) - min(stall_position) +1):

        if distance_OK(stall_position, d, cow_count):

            # tally the largest distance where the arrangement is possible
            stall_count = d
    
    return stall_count
