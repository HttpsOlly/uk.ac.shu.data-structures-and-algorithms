import random as rd
import copy as cp

class Scales:
    def __init__(self, data):
        self.data = data
        self.solution = [rd.randint(0, 1) for _ in range(len(data))]
        self.fitness = 0.00
        self.calculate_fitness()

    # def print_solution(self):
    #     print(self.solution, "\t", self.fitness, "\n")

    def calculate_fitness(self):
        left = sum(weight for weight, side in zip(self.data, self.solution) if side == 0)
        right = sum(weight for weight, side in zip(self.data, self.solution) if side == 1)
        self.fitness = abs(left - right)

    def copy_solution(self, another_scales):
        self.solution = cp.deepcopy(another_scales.solution)
        self.calculate_fitness()    
