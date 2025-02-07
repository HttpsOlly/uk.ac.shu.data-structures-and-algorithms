from plane import Plane
from min_heap import MinHeap

def main():
    priority_queue = MinHeap()

    planes = [
        Plane('D', fuel = 90, distance = 10),
        Plane('C', fuel = 30, distance = 70),
        Plane('B', fuel = 60, distance = 30),
        Plane('A', fuel = 20, distance = 50),
    ]

    for plane in planes:
        priority_queue.min_heap_insert(plane)

        print(f'Adding {plane}')
        print(Plane.get_priority_order(priority_queue))


    while not priority_queue.is_empty():
        next_plane = priority_queue.heap_extract_min()

        print(f"Plane {next_plane.id} is cleared to land.")
        print(Plane.get_priority_order(priority_queue))

if __name__ == "__main__":
    main()
