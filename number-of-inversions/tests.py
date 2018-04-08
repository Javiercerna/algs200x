import random
import time
import unittest

from naive import numberOfInversions as inversionsNaive
from solution import numberOfInversions as inversionsSolution

TIME_LIMIT_SECONDS = 5

class numberOfInversionsTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(inversionsNaive([2, 3, 9, 2, 9]), 2)
        self.assertEqual(inversionsNaive([5, 4, 3, 2, 1]), 10)
        self.assertEqual(inversionsNaive([1, 6, 5]), 1)
        self.assertEqual(inversionsSolution([2, 3, 9, 2, 9]), 2)
        self.assertEqual(inversionsSolution([5, 4, 3, 2, 1]), 10)
        self.assertEqual(inversionsSolution([1, 6, 5]), 1)

    def test_large_inputs(self):
        max_n = int(1e5)
        max_value = 1e9
        nums = [random.randint(1, max_value) for dummy_ind in range(max_n)]
        start_time = time.time()
##        inversionsNaive(nums) # Fails test
        inversionsSolution(nums)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for large inputs (n=%s): %.3f' % \
              (max_n, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        max_n = int(5e3)
        max_value = 1e9
        for dummy_ind in range(100):
            nums = [random.randint(1, max_value) for dummy_ind in range(max_n)]
            print 'First 10 nums: %s' % (nums[:10])
            self.assertEqual(inversionsNaive(nums), inversionsSolution(nums))

if __name__ == '__main__':
    unittest.main()
