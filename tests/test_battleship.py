# Run with python3 -m unittest test_battleship.py
import unittest
from torpydo import ships
from torpydo.ships import Point


class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = ships.Ship("TestShip", 4, "White")

    def test_is_at(self):
        self.ship.all_positions.add(Point(1, 2))

        self.assertTrue(self.ship.receive_fire(Point(1, 2)))

    def test_false(self):
        self.assertFalse(False)

    def test_true(self):
        self.assertTrue(True)

    def test_true2(self):
        self.assertTrue(True)


class TestDummy(unittest.TestCase):
    def setUp(self):
        self.ship = ships.Ship("TestShip", 4, "White")

    def test_false2(self):
        self.assertFalse(False)

    def test_true3(self):
        self.assertTrue(True)

    def test_true4(self):
        self.assertTrue(True)


class TestTDD(unittest.TestCase):
    def setUp(self):
        self.num1 = 1
        self.num2 = 1


    def test_add1_2(self):
        self.assertEqual(3, self.addnums(self.num1, self.num2))

    def test_true3(self):
        self.assertTrue(True)

    def test_true4(self):
        self.assertTrue(True)


if '__main__' == __name__:
    unittest.main()


# test comment hi
