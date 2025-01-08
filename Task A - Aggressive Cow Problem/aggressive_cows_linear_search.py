from itertools import combinations

def min_distance(placement):
    if (len(placement) == 1): return 0
    min_distance = float('inf')
    for i in range(1, len(placement)):
        min_distance = min(min_distance, placement[i] - placement[i - 1])
    return min_distance

def aggressive_cows_linear_search(stall_position, cow_count):
    largest_min_distance = 0
    for placement in combinations(stall_position, cow_count):
        largest_min_distance = max(largest_min_distance, min_distance(placement))
    return largest_min_distance