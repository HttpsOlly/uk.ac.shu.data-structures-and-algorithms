def heap_sort_algorithm(data):
    def max_heapify(arr, heap_size, root):
        biggest = root
        left = (2 * root) + 1
        right = (2 * root) + 2

        if left < heap_size and arr[left] > arr[biggest]:
            biggest = left

        if right < heap_size and arr[right] > arr[biggest]:
            biggest = right

        if biggest != root:
            arr[root], arr[biggest] = arr[biggest], arr[root]
            max_heapify(arr, heap_size, biggest)

    n = len(data)

    for i in range(n//2 - 1, -1, -1):
        max_heapify(data, n, i)

    for i in range(n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        max_heapify(data, i, 0)

    return data

"""
Pseudocode inspiration from Cormen et al (2009)

References:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction To Algorithms (3rd ed). MIT Press.
"""