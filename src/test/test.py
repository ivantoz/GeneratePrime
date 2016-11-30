import unittest
from primenumbers import generate_prime

class TestGeneratePrimeMethod(unittest.TestCase):
    def test_correctresult(self):
        self.assertSequenceEqual(generate_prime(10), [2,3,5,7])

    def test_negative(self):
        self.assertEqual(generate_prime(-5), 'Negative numbers cannot be prime numbers')

    def test_less_than_two(self):
        self.assertEqual(generate_prime(1), 'No prime number below 2')

    def test_stringInput(self):
        self.assertEqual(generate_prime('hundred'), 'Cannot find prime of non integer')


if __name__ == '__main__':
    unittest.main()




