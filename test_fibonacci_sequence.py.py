import unittest
from fibonacci_sequence import*

class Tests(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), "0 1 1 2 3 5 8 ")

if __name__ == "__main__":
    unittest.main()