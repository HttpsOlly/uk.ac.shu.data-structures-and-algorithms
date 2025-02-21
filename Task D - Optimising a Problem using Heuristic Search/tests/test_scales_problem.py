import unittest
from scales_problem import Scales

class TestScalesProblem(unittest.TestCase):
    
    def setUp(self):
        self.data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
        self.scales = Scales(self.data)
    
    def test_initial_solution(self):
        self.assertEqual(len(self.scales.solution), len(self.data))
        self.assertIsInstance(self.scales.solution, list)
        self.assertTrue(all(bit in [0, 1] for bit in self.scales.solution))
    
    def test_calculate_fitness(self):
        self.scales.calculate_fitness()
        left = sum(weight for weight, side in zip(self.data, self.scales.solution) if side == 0)
        right = sum(weight for weight, side in zip(self.data, self.scales.solution) if side == 1)
        expected_fitness = abs(left - right)
        self.assertEqual(self.scales.fitness, expected_fitness)
    
    def test_copy_solution(self):
        new_scales = Scales(self.data)
        new_scales.solution = [1 - bit for bit in self.scales.solution]
        new_scales.calculate_fitness()
        self.scales.copy_solution(new_scales)
        self.assertEqual(self.scales.solution, new_scales.solution)
        self.assertEqual(self.scales.fitness, new_scales.fitness)

if __name__ == '__main__':
    unittest.main()