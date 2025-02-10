import unittest
from heap_sort import heap_sort_algorithm

class TestHeapSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_collection(self):
        self.assertEqual(heap_sort_algorithm([]), [])

    def test_single_item_collection(self):
        self.assertEqual(heap_sort_algorithm([0]), [0])

    def test_ordered_two_item_collection(self):
        self.assertEqual(heap_sort_algorithm([0,1]), [0,1])

    def test_unordered_two_item_collection(self):
        self.assertEqual(heap_sort_algorithm([1,0]), [0,1])

    def test_unordered_ten_item_collection(self):
        self.assertEqual(heap_sort_algorithm([9,8,7,6,5,4,3,2,1,0]), [0,1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()