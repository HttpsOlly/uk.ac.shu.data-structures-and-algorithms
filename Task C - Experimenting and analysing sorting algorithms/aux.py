import random, time, csv

def append_result(row, filename="sorted_results.csv"):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

def generate_dataset(size):
    return random.sample(range(0, 100001), size)

def print_sorted_data(data, sort_duration_ns, algorithm_name, size):
    print(data)
    print(f"{algorithm_name} completed for {size} in {sort_duration_ns} nanoseconds")

def read_dataset(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        dataset = [int(row[0]) for row in reader]
    return dataset

def sort_algorithm_timing(algorithm, data):
    start_sort = time.time_ns()
    algorithm(data)
    end_sort = time.time_ns()
    return end_sort - start_sort

def write_random_dataset_to_csv(dataset, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for data in dataset:
            writer.writerow([data])

def create_results_csv(result, filename="sorted_results.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Dataset Size", "Sort Method", "Duration (nanoseconds)"])
        for row in result:
            writer.writerow(row)
