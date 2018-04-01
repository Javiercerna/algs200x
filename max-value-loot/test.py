import unittest
import random
import time

from solution import sortItemsByValueWeightRatio as sortItems
from solution import maxValueOfLoot as maxValueSolution

TIME_LIMIT_SECONDS = 5
EPSILON = 1e-3
MAX_N = 1000
MAX_VALUE = 2e6
MAX_WEIGHT = 2e6
MAX_KNAPSACK_CAPACITY = 2e6

class MaxValueOfLootTest(unittest.TestCase):
    def test_sortItemsByValueWeightRatio(self):
        self.assertEqual(sortItems([(10, 10)]), [(10, 10)])
        self.assertEqual(sortItems([(60, 20), (100, 50)]), [(100, 50), (60, 20)])
        self.assertEqual(sortItems([(21, 22), (2, 3), (11, 12)]),
                        [(2, 3), (11, 12), (21, 22)])
        self.assertEqual(sortItems([(447, 155), (1023, 50)]), [(447, 155), (1023, 50)])
        items = [(random.randint(1, MAX_VALUE), random.randint(1, MAX_WEIGHT)) for
                  dummy_ind in range(MAX_N)]
        start_time = time.time()
        sortItems(items)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds to sort max inputs (n=%s): %.3f' % \
              (MAX_N, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)
        
    def test_trivial_case(self):
        solution = maxValueSolution(50, [(60, 20), (100, 50), (120, 30)]) 
        self.assertTrue(solution - 180 < EPSILON)
        self.assertTrue(maxValueSolution(10, [(500, 30)]) - 166.6667 < EPSILON)

    def test_max_inputs(self):
        items = [(random.randint(1, MAX_VALUE), random.randint(1, MAX_WEIGHT)) for
                  dummy_ind in range(MAX_N)]
        start_time = time.time()
        maxValueSolution(MAX_KNAPSACK_CAPACITY, items)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max inputs (n=%s): %.3f' % \
              (MAX_N, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)
        
if __name__ == '__main__':
    unittest.main()
