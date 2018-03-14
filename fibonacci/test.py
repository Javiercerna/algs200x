import random
import time
import unittest

from naive import fibonacci as fibonacciNaive
from solution import fibonacci as fibonacciSolution

TIME_LIMIT_SECONDS = 5

class FibonacciTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(5, fibonacciNaive(5))
        self.assertEqual(55, fibonacciNaive(10))

    def test_large_inputs(self):
        n = 100
        start_time = time.time()
##        fibonacciNaive(n) # Fails test
        fibonacciSolution(n)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for large input (n=%s): %.3f' % \
              (n, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for n in range(35):
            self.assertEqual(fibonacciNaive(n), fibonacciSolution(n))

if __name__ == '__main__':
    unittest.main()
