def distance_OK(stall_position, distance, cow_count):

    # start by assuming we can place one cow
    cows_placed = 1
    previous_position = stall_position[0]

    # for each distance, begin by placing cows at the first stall and check...
    for pos in range(1, len(stall_position)):
        current_position = stall_position[pos]

        # if distance is greater than known largest distance
        if current_position - previous_position >= distance:

            # can place cow here
            cows_placed += 1

            # bump the previous position to be current cow placement
            previous_position = current_position

            # have we placed all cows?
            if cows_placed == cow_count:
                return True

    return False

