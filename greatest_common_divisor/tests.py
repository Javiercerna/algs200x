import random
import time
import unittest

from naive import GCD as GCDNaive
from solution import GCD as GCDSolution

TIME_LIMIT_SECONDS = 5

class GCDTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(GCDNaive(18, 35), 1)
        self.assertEqual(GCDNaive(1344, 217), 7)
        self.assertEqual(GCDNaive(28851538, 1183019), 17657)
        self.assertEqual(GCDSolution(18, 35), 1)
        self.assertEqual(GCDSolution(1344, 217), 7)
        self.assertEqual(GCDSolution(28851538, 1183019), 17657)

    def test_max_inputs(self):
        max_input = int(2e9)
        start_time = time.time()
##        GCDNaive(1, max_input) # Fails test
        GCDSolution(1, max_input)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max inputs (1, %s): %.3f' % \
              (max_input, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for dummy_ind in range(100):
            a = random.randint(1, 2e6)
            b = random.randint(1, 2e6)
            print a, b
            self.assertEqual(GCDNaive(a, b), GCDSolution(a, b))

if __name__ == '__main__':
    unittest.main()
        
