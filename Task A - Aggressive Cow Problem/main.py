import random
import time
from aggressive_cows import aggressive_cows

def main():
    data_set_sizes = [5, 10, 15, 20, 25, 30, 35, 40]
    random_spread_size = random.choice( range(2, 5) )
    for data_set_size in data_set_sizes:
        random_data_set = random.sample( range (1, random_spread_size * (data_set_size+1)), data_set_size) 
        serial_cow_count = list( range (1, data_set_size+1))
        print (f"{data_set_size} stalls with a random spread size of {random_spread_size}: {random_data_set} ")

        for cow_count in serial_cow_count:

            for method in ['linear', 'binary']:
                benchmark_time_start = time.time()
                aggressive_cows (random_data_set, cow_count, method)
                benchmark_time_end = time.time()
                print (f"Place {cow_count} cows into {data_set_size} stalls ({method}): {(benchmark_time_end - benchmark_time_start):.6f} seconds")

                # stalls, cows, method, duration
                # 20, 1, linear, 0.00001
                # 20, 1, binary, 0.00001
                # 20, 2, linear, 0.00001
                # 20, 2, binary, 0.00001

if __name__ == "__main__":
    main()
