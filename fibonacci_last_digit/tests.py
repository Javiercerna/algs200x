import random
import time
import unittest

from naive import fibonacci_last_digit as lastDigitNaive
from solution import fibonacci_last_digit as lastDigitSolution

TIME_LIMIT_SECONDS = 5

class FibonacciLastDigitTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(lastDigitNaive(3), 2)
        self.assertEqual(lastDigitNaive(331), 9)
        self.assertEqual(lastDigitSolution(3), 2)
        self.assertEqual(lastDigitSolution(331), 9)
        self.assertEqual(lastDigitSolution(327305), 5)

    def test_large_inputs(self):
        n = int(1e7)
        start_time = time.time()
##        lastDigitNaive(n) # Fails test
        lastDigitSolution(n)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for large input (n=%s): %.3f' % \
              (n, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for dummy_ind in range(100):
            n = random.randint(2,1e5)
            print n
            self.assertEqual(lastDigitNaive(n), lastDigitSolution(n))

if __name__ == '__main__':
    unittest.main()
