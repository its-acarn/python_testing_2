import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Smirnoff", 4.50, 35)

    def test_drink_has_name(self):
        self.assertEqual("Smirnoff", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(4.50, self.drink.price)