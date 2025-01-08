import unittest
from aggressive_cows import aggressive_cows

class TestAggressiveCows(unittest.TestCase):
    def setUp(self):
        self.methods = ['binary', 'linear']
        print (self._testMethodName)

    def test_aggressive_cows(self):
        stalls = [1, 2, 4, 8, 9]
        cows = 3
        expected_results = 3
        for method in self.methods:
            self.assertEqual(aggressive_cows(stalls, cows, method), expected_results)

    def test_minimum_distance(self):
        stalls = [1, 2, 3, 4, 5]
        cows = 2
        expected_results = 4
        for method in self.methods:
            self.assertEqual(aggressive_cows(stalls, cows, method), expected_results)

    def test_equal_distance(self):
        stalls = [1, 3, 5, 7, 9]
        cows = 3
        expected_results = 4
        for method in self.methods:
            self.assertEqual(aggressive_cows(stalls, cows, method), expected_results)

    def test_large_number_of_stalls(self):
        stalls = [1, 2, 4, 8, 16, 32, 64]
        cows = 4
        expected_results = 15
        for method in self.methods:
            self.assertEqual(aggressive_cows(stalls, cows, method), expected_results)

    def test_single_stall(self):
        stalls = [1]
        cows = 1
        expected_results = 0
        for method in self.methods:
            self.assertEqual(aggressive_cows(stalls, cows, method), expected_results)

    def test_two_stalls(self):
        stalls = [1, 10]
        cows = 2
        expected_results = 9
        for method in self.methods:
            self.assertEqual(aggressive_cows(stalls, cows, method), expected_results)

    def test_unsorted_stalls(self):
        stalls = [1, 2, 8, 4, 9]
        cows = 3
        expected_results = 3
        for method in self.methods:
            self.assertEqual(aggressive_cows(stalls, cows, method), expected_results)

if __name__ == '__main__':
    unittest.main()