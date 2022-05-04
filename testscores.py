###############################################################
# These unit tests check score behaviour in 'scoresheeets.py' #
###############################################################
import unittest

import dice


# test properties of Die
class DieTests(unittest.TestCase):
    def setUp(self):
        # random dice
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)
        # one of each value
        self.d6_1 = dice.Die(6,1)
        self.d6_2 = dice.Die(6,2)
        self.d6_3 = dice.Die(6,3)
        self.d6_4 = dice.Die(6,4)
        self.d6_5 = dice.Die(6,5)
        self.d6_6 = dice.Die(6,6)

    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertEqual(self.d8.sides, 8)
        self.assertIn(self.d6.value, range(1, 7))
        self.assertIn(self.d6.value, range(1,9))

    def test_eq(self):
        self.assertEqual(self.d6_1, self.d6_1 , 'Failed __eq__ test')

    def test_ne(self):
        self.assertNotEqual(self.d6_1, self.d6_2, 'Failed __ne__ test')

    def test_gt(self):
        self.assertGreater(self.d6_2, self.d6_1, 'Failed __gt__ test')

    def test_lt(self):
        self.assertLess(self.d6_1, self.d6_2, 'failed __lt__ test')

    def test_ge(self):
        self.assertGreaterEqual(self.d6_2, self.d6_2, 'Failed __ge__ test')
        self.assertGreaterEqual(self.d6_3, self.d6_2, 'Failed __ge__ test')

    def test_le(self):
        self.assertLessEqual(self.d6_2, self.d6_2, 'Failed __le__ test')
        self.assertLessEqual(self.d6_1, self.d6_2, 'Failed __le__ test')

    def test_add(self):
        self.assertIsInstance(self.d6+self.d8, int, 'Faied __add__ test')

    def test_radd(self):
        self.assertIsInstance(3 + self.d6, int, 'Failed __radd__ test')

    def test_repr(self):
        self.assertEqual(str(self.d6_4), '4', 'Failed __repr__ test')

    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            dice.Die(1)


# test D6
class D6Tests(unittest.TestCase):
    def setUp(self):
        self.d1 = dice.D6()
        self.d2 = dice.D6()

    # only need to test that a D6 has 6 sides
    def test_creation(self):
        self.assertEqual(self.d1.sides, 6, 'D6 sides')
        self.assertEqual(self.d2.sides, 6, 'D6 sides')
        self.assertIn(self.d1.value, range(1, 7), 'D6 range')
        self.assertIn(self.d2.value, range(1, 7), 'D6 range')

    # we do have two D6's that can be added. No need for other tests
    # as 'D6' is based on parent class 'Die'
    def test_add(self):
        self.assertIsInstance(self.d1+self.d2, int, 'D6 __add__ test')


if __name__ == '__main__':
    unittest.main()
