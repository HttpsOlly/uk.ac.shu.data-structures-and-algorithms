import aux
import hill_climbing as hc

def start_hill_climbing():
    try:
        provided_dataset = "data/dataset.csv"
        data = aux.read_dataset_csv(provided_dataset)
        hc.run_rrhc(data)
    except Exception as e:
        print(f"Unknown error occurred {e}")

if __name__ == "__main__":
    start_hill_climbing()