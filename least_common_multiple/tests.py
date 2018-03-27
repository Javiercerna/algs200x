import random
import time
import unittest

from naive import LCM as LCMNaive
from solution import LCM as LCMSolution

TIME_LIMIT_SECONDS = 5

class LCMTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(LCMNaive(6, 8), 24)
        self.assertEqual(LCMNaive(40, 50), 200)
        self.assertEqual(LCMNaive(1324, 3975), 5262900)
        self.assertEqual(LCMSolution(6, 8), 24)
        self.assertEqual(LCMSolution(40, 50), 200)
        self.assertEqual(LCMSolution(1324, 3975), 5262900)
        self.assertEqual(LCMSolution(28851538, 1183019), 1933053046)

    def test_max_inputs(self):
        max_input = int(2e9)
        start_time = time.time()
##        LCMNaive(max_input, max_input) # Fails test
        LCMSolution(max_input, max_input-1)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max inputs (%s, %s): %.3f' % \
              (max_input, max_input-1, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for dummy_ind in range(100):
            a = random.randint(1, 2e3)
            b = random.randint(1, 2e3)
            print a, b
            self.assertEqual(LCMNaive(a, b), LCMSolution(a, b))
        
if __name__ == '__main__':
    unittest.main()
