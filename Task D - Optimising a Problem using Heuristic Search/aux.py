import csv

def read_dataset_csv(file):
    try:
        with open(file, mode="r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            first_row = next(csv_reader)
            float_list = [float(num) for num in first_row]
            return float_list
    except FileNotFoundError:
        print("Dataset not found")

def write_result(results):
    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Restart", "Iteration", "Fitness", "Solution"])
        for row in results:
            writer.writerow(row)