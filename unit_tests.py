import unittest
from calculator import cal, add

class TestCalculator(unittest.TestCase):

    def setUp(self):
        #Set up testing objects
        self.a = 439
        self.b = 4

    def test_add(self):
        print('Testing add method')
        calculator = cal(self.a, self.b)

        self.assertEqual(calculator.add(),443)

    def test_subtract(self):
        print('Testing subtract method')
        calculator = cal(self.a, self.b)
        self.assertEqual(calculator.sub(), 435)

class TestAdd(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add([1,2,3]), 6)


if __name__ == '__main__':
    unittest.main(verbosity=2)
