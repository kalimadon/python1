import unittest

def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

class TestFibGenerator(unittest.TestCase):

    def test_fib_generator(self):
        fib = fib_generator()
        expected_fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for fib_num in expected_fib_sequence:
            self.assertEqual(next(fib), fib_num)

if name == 'main':
    unittest.main()