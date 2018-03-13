import random
import time
import unittest

from naive import computeMaxPairwiseProduct as computeNaive
from solution import computeMaxPairwiseProduct as computeSolution

TIME_LIMIT_SECONDS = 5

class MaxPairwiseProductTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(6, computeNaive([3, 2]))
        self.assertEqual(6, computeNaive([2, 3]))

    def test_max_inputs(self):
        max_inputs = int(2*10e5) * [2*10e5]
        
        start_time = time.time()
##        computeNaive(max_inputs) # Fails test
        computeSolution(max_inputs)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max inputs: %.3f' % (elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for dummy_ind in range(100):
            list_length = random.randint(2, 1000)
            inputs = [random.randint(0, 2*10e5) for x in xrange(list_length)]
            print inputs
            self.assertEqual(computeNaive(inputs), computeSolution(inputs))

if __name__ == '__main__':
    unittest.main()
