def distance_OK(stall_position, distance, cow_count):
    cows_placed = 1
    last_position = stall_position[0]

    for i in range(1, len(stall_position)):
        if stall_position[i] - last_position >= distance:
            cows_placed += 1
            last_position = stall_position[i]
            if cows_placed == cow_count:
                return True
    return False

def aggressive_cows_binary_search(stall_position, cow_count):
    stall_position.sort()
    low = 1
    high = stall_position[-1] - stall_position[0]
    stall_count = 0

    while low <= high:
        d = (low + high) // 2
        if distance_OK(stall_position, d, cow_count):
            stall_count = d
            low = d + 1
        else:
            high = d - 1

    return stall_count

