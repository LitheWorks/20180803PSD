# Run with python3 -m unittest test_battleship.py
import unittest
from torpydo import mathtest


class TestTDD(unittest.TestCase):
    def setUp(self):
        self.MathTest = mathtest.MathTest()

    def test_add1_2(self):
#        self.assertTrue(True)
        self.assertEqual(3, self.MathTest.addnums(1, 2))

    def test_add3_4(self):
        self.assertEqual(7, self.MathTest.addnums(3, 4))


if '__main__' == __name__:
    unittest.main()


# test comment hi
