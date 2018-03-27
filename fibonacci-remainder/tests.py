import random
import time
import unittest

from naive import fibonacciRemainder as remainderNaive
from solution import findPisanoPeriod
from solution import fibonacciRemainder as remainderSolution

TIME_LIMIT_SECONDS = 5

class FibonacciRemainderTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(remainderNaive(0, 4349), 0)
        self.assertEqual(remainderNaive(15, 2), 0)
        self.assertEqual(remainderNaive(13, 3), 2)
        self.assertEqual(remainderNaive(239, 1000), 161)
        self.assertEqual(remainderSolution(0, 4349), 0)
        self.assertEqual(remainderSolution(15, 2), 0)
        self.assertEqual(remainderSolution(13, 3), 2)
        self.assertEqual(remainderSolution(239, 1000), 161)
        self.assertEqual(remainderSolution(2816213588, 30524), 10249)

    def test_findPisanoPeriod(self):
        self.assertEqual(findPisanoPeriod(1), 2)
        self.assertEqual(findPisanoPeriod(2), 3)
        self.assertEqual(findPisanoPeriod(3), 8)
        self.assertEqual(findPisanoPeriod(377), 28)
        self.assertEqual(findPisanoPeriod(1000), 1500)
        self.assertEqual(findPisanoPeriod(10000), 15000)
        self.assertEqual(findPisanoPeriod(100000), 150000)
        self.assertEqual(findPisanoPeriod(46368), 48)
    
    def test_max_inputs(self):
        max_n = int(1e18)
        max_divisor = int(1e5)
        start_time = time.time()
##        remainderNaive(max_n, max_divisor) # Fails test
        remainderSolution(max_n, max_divisor)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max inputs (n=%s, divisor=%s): %.3f' % \
              (max_n, max_divisor, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

    def test_stress(self):
        for dummy_ind in range(100):
            n = random.randint(1, 1e5)
            divisor = random.randint(1, 1e5)
            print n, divisor
            self.assertEqual(remainderNaive(n, divisor), remainderSolution(n, divisor))
        
if __name__ == '__main__':
    unittest.main()
