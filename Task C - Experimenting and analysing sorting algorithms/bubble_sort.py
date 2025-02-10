def bubble_sort_algorithm(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break
    return data

"""
Pseudocode inspiration from Cormen et al (2009)

References:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction To Algorithms (3rd ed). MIT Press.
"""