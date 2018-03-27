import random
import time
import unittest

from naive import fibonacciSumLastDigit as lastDigitNaive
from solution import fibonacciSumLastDigit as lastDigitSolution

TIME_LIMIT_SECONDS = 5

class FibonacciSumLastDigitTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(lastDigitNaive(3, 7), 1)
        self.assertEqual(lastDigitNaive(10, 10), 5)
        self.assertEqual(lastDigitNaive(10, 200), 2)
        self.assertEqual(lastDigitSolution(3, 7), 1)
        self.assertEqual(lastDigitSolution(10, 10), 5)
        self.assertEqual(lastDigitSolution(10, 200), 2)
        
    def test_large_inputs(self):
        m = int(1e17)
        n = int(1e18)
        start_time = time.time()
##        lastDigitNaive(n) # Fails test
        lastDigitSolution(m, n)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for large input (m=%s, n=%s): %.3f' % \
              (m, n, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for dummy_ind in range(100):
            m = random.randint(2, 1e7)
            n = random.randint(m, 1e7)
            print m, n
            self.assertEqual(lastDigitNaive(m, n), lastDigitSolution(m, n))

if __name__ == '__main__':
    unittest.main()
