import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Smirnoff", 4.50)

    def test_drink_has_name(self):
        self.assertEqual("Smirnoff", self.drink.name)