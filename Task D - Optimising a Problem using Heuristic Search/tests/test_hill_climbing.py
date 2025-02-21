import unittest
import random
from hill_climbing import Hill_Climbing, run_rrhc, flip_bits, print_sum_of_scales

class TestHillClimbing(unittest.TestCase):
    
    def setUp(self):
        self.data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
        self.hc = Hill_Climbing(self.data)
    
    def test_initial_solution(self):
        self.assertEqual(len(self.hc.solution1.solution), len(self.data))
        self.assertEqual(len(self.hc.solution2.solution), len(self.data))
        self.assertEqual(self.hc.solution1.solution, self.hc.solution2.solution)
    
    def test_small_change(self):
        original_solution = self.hc.solution2.solution.copy()
        self.hc.small_change()
        self.assertNotEqual(self.hc.solution2.solution, original_solution)
    
    def test_flip_bits_simple(self):
        new_solution = flip_bits(self.data, 50)
        self.assertEqual(len(new_solution), len(self.data))
        self.assertNotEqual(self.data, new_solution)

    def test_flip_bits_detail(self):
        # assemble
        test_solution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        flip_percentage = 50 
        flipped_count = 0
        random.seed(0)

        # action
        flipped_solution = flip_bits(test_solution, flip_percentage)

        # assert
        for original_bit, flipped_bit in zip(test_solution, flipped_solution):
            if original_bit != flipped_bit:
                flipped_count += 1
        expected_count = int(len(test_solution) * flip_percentage / 100)
        self.assertEqual(flipped_count, expected_count)
    
if __name__ == '__main__':
    unittest.main()