import random
import time
import unittest

from naive import maxAdRevenue as maxRevenueNaive
from solution import maxAdRevenue as maxRevenueSolution

TIME_LIMIT_SECONDS = 5

class MaxAdRevenueTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(maxRevenueNaive([23], [39]), 897)
        self.assertEqual(maxRevenueNaive([1, 3, -5], [-2, 4, 1]), 23)
        self.assertEqual(maxRevenueSolution([23], [39]), 897)
        self.assertEqual(maxRevenueSolution([1, 3, -5], [-2, 4, 1]), 23)

    def test_max_inputs(self):
        max_n = 1000
        profits = [random.randint(-1e5, 1e5) for dummy_ind in range(max_n)]
        clicks = [random.randint(-1e5, 1e5) for dummy_ind in range(max_n)]
        start_time = time.time()
##        maxRevenueNaive(profits, clicks) # Fails test
        maxRevenueSolution(profits, clicks)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max inputs (n=%s): %.3f' % \
              (max_n, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        n = 8
        for dummy_ind in range(100):
            profits = [random.randint(-1e5, 1e5) for dummy_ind in range(n)]
            clicks = [random.randint(-1e5, 1e5) for dummy_ind in range(n)]
            print profits, clicks
            self.assertEqual(maxRevenueNaive(profits, clicks),
                             maxRevenueSolution(profits, clicks))

if __name__ == '__main__':
    unittest.main()
