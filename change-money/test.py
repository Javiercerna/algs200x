import unittest
import time

from solution import changeMoney

TIME_LIMIT_SECONDS = 5

class ChangeMoneyTest(unittest.TestCase):
    def test_trivial_case(self):
        self.assertEqual(changeMoney(2), 2)
        self.assertEqual(changeMoney(28), 6)
        self.assertEqual(changeMoney(997), 102)

    def test_max_input(self):
        max_input = 999
        start_time = time.time()
        changeMoney(max_input)
        elapsed_seconds = time.time() - start_time
        print '\nElapsed seconds for max input (m=%s): %.3f' % \
              (max_input, elapsed_seconds)
        self.assertTrue(elapsed_seconds < TIME_LIMIT_SECONDS)

if __name__ == '__main__':
    unittest.main()
