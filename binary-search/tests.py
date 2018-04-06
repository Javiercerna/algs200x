import random
import time
import unittest

from solution import binarySearch

TIME_LIMIT_SECONDS = 5

class BinarySearchTest(unittest.TestCase):
    def test_trivial_case(self):
        nums = [1, 5, 8, 12, 13]
        low = 0
        high = len(nums)-1
        self.assertEqual(binarySearch(8, nums, low, high), 2)
        self.assertEqual(binarySearch(1, nums, low, high), 0)
        self.assertEqual(binarySearch(23, nums, low, high), -1)
        self.assertEqual(binarySearch(6, nums, low, high), -1)

    def test_max_inputs(self):
        n = int(1e4)
        max_num = 1e9
        nums = [random.randint(1, max_num) for dummy_ind in range(n)]
        nums.sort()
        keys = [random.randint(1, max_num) for dummy_ind in range(n)]
        start_time = time.time()
        for key in keys:
            binarySearch(key, nums, 0, n-1)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max inputs (n=%s): %.3f' % \
              (n, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        n = int(1e4)
        max_num = 1e9
        for dummy_ind in range(1000):
            nums = [random.randint(1, max_num) for dummy_ind in range(n)]
            nums.sort()
            key = random.randint(1, max_num)
            if key not in nums:
                print key
                self.assertEqual(binarySearch(key, nums, 0, n-1), -1)

if __name__ == '__main__':
    unittest.main()
