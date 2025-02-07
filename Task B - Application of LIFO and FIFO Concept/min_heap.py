class MinHeap:
    # derived from Max Heap pseudocode in 
    # Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms (3rd ed.). MIT Press.

    def __init__(self):
        self.heap = []

    def min_heap_insert(self, key):
        self.heap.append(key)
        self.heap_decrease_key(len(self.heap) - 1, key)

    def heap_decrease_key(self, i, key):
        if key > self.heap[i]:
            raise ValueError("New key is larger than current key")
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heap_extract_min(self):
        if self.is_empty():
            raise IndexError("Heap underflow")
        smallest = self.heap[0]
        self.swap(0,len(self.heap) -1)
        self.heap.pop()
        self.min_heapify(0)
        return smallest

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)
    
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0