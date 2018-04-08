import random
import time
import unittest

from solution import mergeSort

TIME_LIMIT_SECONDS = 5
max_n = int(1e5)
max_value = 1e9

class mergeSortTest(unittest.TestCase):
    def test_trivial_cases(self):
        self.assertEqual(mergeSort([2, 3, 9, 2, 9]), [2, 2, 3, 9, 9])
        self.assertEqual(mergeSort([1, 6, 5]), [1, 5, 6])
        self.assertEqual(mergeSort([1]), [1])
        self.assertEqual(mergeSort([3, 3, 3, 3]), [3, 3, 3, 3])

    def test_large_inputs(self):
        nums = [random.randint(1, max_value) for dummy_ind in range(max_n)]
        start_time = time.time()
        mergeSort(nums)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for large inputs (n=%s): %.3f' % \
              (max_n, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for dummy_ind in range(100):
            nums = [random.randint(1, max_value) for dummy_ind in range(max_n)]
            print 'First 10 nums: %s' % (nums[:10])
            self.assertEqual(mergeSort(nums), sorted(nums))
        
if __name__ == '__main__':
    unittest.main()
