# Used inspiration from https://github.com/zairulmazwan/Tutorial6_Heuristic_Python/blob/main/Hill_Climbing.py

import scales_problem as sp
import random
import aux

num_of_restarts = 20
num_of_iterations = 4000

def run_rrhc(data):
    best_solution = []
    best_fitness = float("inf")
    results = []

    for restart in range(num_of_restarts):
        hc = Hill_Climbing(data)
        for i in range(num_of_iterations):
            # print(f"Iteration number {i}")
            hc.small_change()
            # print("New solution: \n")
            # self.solution2.print_solution()
            # print("Current solution: \n")
            # self.solution1.print_solution()
            if hc.solution2.fitness < hc.solution1.fitness:
                hc.solution1.copy_solution(hc.solution2)

            row = [restart + 1, i + 1, hc.solution1.fitness, hc.solution1.solution.copy()]
            results.append(row)

        if hc.solution1.fitness < best_fitness:
            best_solution = hc.solution1.solution.copy()
            best_fitness = hc.solution1.fitness

        print(f"Restart {restart + 1} complete")    

    aux.write_result(results)

    print("Best Solution: \n", best_solution)
    print_sum_of_scales(best_solution, data)
    print("Best Fitness: \n", best_fitness)

def flip_bits(solution, percentage):
    number_of_bits_to_flip = int(len(solution) * percentage / 100)
    new_solution = solution.copy()

    index_numbers_to_flip = random.sample(range(len(new_solution)), number_of_bits_to_flip)

    for index in index_numbers_to_flip:
        new_solution[index] = 1 - new_solution[index]
    
    return new_solution
    
def print_sum_of_scales(solution, data):
    left_total = sum(weight for weight, side in zip(data, solution) if side == 0)
    right_total = sum(weight for weight, side in zip(data, solution) if side == 1)
    print(f"Weight of left side: {left_total:.6f}")
    print(f"Weight of right side: {right_total:.6f}")
    print(f"Difference in scales: {abs(left_total - right_total):.6f}")

class Hill_Climbing:
    def __init__(self, data):
        self.solution1 = sp.Scales(data)
        self.solution2 = sp.Scales(data)
        self.solution2.copy_solution(self.solution1)

    def small_change(self):
        self.solution2.solution = flip_bits(self.solution2.solution, 10)
        self.solution2.calculate_fitness()
