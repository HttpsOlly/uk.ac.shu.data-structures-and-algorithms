import random
import time
from aggressive_cows import aggressive_cows

def main():
    data_set_sizes = [10, 20, 30, 50, 100, 1000, 10000]
    for data_set_size in data_set_sizes:
        random_data_set = random.sample( range (1, data_set_size+1), data_set_size) 
        random_cow_count = random.choice( range (1, data_set_size+1)) 

        for method in ['linear', 'binary']:
            benchmark_time_start = time.time()
            aggressive_cows (random_data_set, random_cow_count, method)
            benchmark_time_end = time.time()
            print (f"{data_set_size} stalls ({method}): {benchmark_time_end - benchmark_time_start} milliseconds")

        # try:
            # do performance testing stuff 
        #except ValueError as e:
            #

if __name__ == "__main__":
    main()
