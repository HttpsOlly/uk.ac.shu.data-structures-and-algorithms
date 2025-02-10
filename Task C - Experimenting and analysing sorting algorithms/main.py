import bubble_sort, heap_sort, aux

def run_both_sorting_algorithms():
    dataset_sizes = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]

    aux.create_results_csv([], "sorted_results.csv")
    
    for size in dataset_sizes:
        for _ in range(5):
            data = aux.generate_dataset(size)

            dataset_filename = f"dataset_{size}.csv"
            aux.write_random_dataset_to_csv(data, dataset_filename)

            bubble_sort_data = aux.read_dataset(dataset_filename)
            heap_sort_data = aux.read_dataset(dataset_filename)

            # Bubble Sort
            bubble_sort_duration_ns = aux.sort_algorithm_timing(bubble_sort.bubble_sort_algorithm, bubble_sort_data)
            aux.print_sorted_data(bubble_sort_data, bubble_sort_duration_ns, "Bubble Sort", size)
            aux.append_result([size, "Bubble", bubble_sort_duration_ns])

            # Heap Sort
            heap_sort_duration_ns = aux.sort_algorithm_timing(heap_sort.heap_sort_algorithm, heap_sort_data)
            aux.print_sorted_data(heap_sort_data, heap_sort_duration_ns, "Heap Sort", size)
            aux.append_result([size, "Heap", heap_sort_duration_ns])

if __name__ == "__main__":
    run_both_sorting_algorithms()