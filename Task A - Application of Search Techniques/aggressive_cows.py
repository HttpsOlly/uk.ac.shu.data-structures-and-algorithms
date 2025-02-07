from aggressive_cows_binary_search import aggressive_cows_binary_search
from aggressive_cows_linear_search import aggressive_cows_linear_search

def aggressive_cows(stall_position, cow_count, method):
    if method == 'binary':
        return aggressive_cows_binary_search(stall_position, cow_count)
    elif method == 'linear':
        return aggressive_cows_linear_search(stall_position, cow_count)
    else:
        raise ValueError("Invalid method. Choose 'binary' or 'linear'.")

