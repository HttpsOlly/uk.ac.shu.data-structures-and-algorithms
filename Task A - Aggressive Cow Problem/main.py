import random
import time
from aggressive_cows import aggressive_cows

def main():

    # create a testable collection of stall position sizes
    stall_position_sizes = [10, 100, 1000, 10000, 100000]

    # introduce a random spread to give the stall positions some gaps
    random_spread_size = random.choice( range(2, 5) )

    # start writing a CSV of benchmarks
    timestamp = time.strftime('%Y%m%dT%H%M%S')
    with open(f"benchmark-{timestamp}.csv", 'a') as file:
        file.write('stalls,cows,method,duration' + '\n')

    # test each number of stall positions in the testable collection
    for stall_position_size in stall_position_sizes:

        # unordered random distribution of stalls 
        spreaded_stall_position = range(1, random_spread_size * (stall_position_size+1))
        stall_position = random.sample(spreaded_stall_position, stall_position_size) 

        # create an iterable sequence of the number of cows from 1 through to the number of stalls
        step_size = stall_position_size // 10
        serial_cow_count = list(range(1, stall_position_size+1, step_size))
    
        print(f"{stall_position_size} stalls with a random spread size of {random_spread_size}: {stall_position[:100]} ")

        # iterate the number of cows
        for cow_count in serial_cow_count:

            # exercise both methods 
            for method in ['linear', 'binary']:

                # start timer
                benchmark_time_start = time.time()

                largest_minimum_distance = aggressive_cows(stall_position, cow_count, method)
                
                # end timer
                benchmark_time_end = time.time()
                duration = benchmark_time_end - benchmark_time_start

                print(f"Place {cow_count} cows into {stall_position_size} stalls ({method}): {duration:.6f} seconds")

                # write benchmark to CSV 
                with open(f"benchmark-{timestamp}.csv", 'a') as file:
                    file.write(f"{stall_position_size},")
                    file.write(f"{cow_count},")
                    file.write(f"{largest_minimum_distance},")
                    file.write(f"{method},")
                    file.write(f"{duration}\n")

if __name__ == "__main__":
    main()
