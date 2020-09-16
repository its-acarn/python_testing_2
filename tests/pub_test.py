import unittest
from src.pub import Pub 
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.drink_1 = Drink("Tennents", 3.40)
        self.drink_2 = Drink("Wine", 7.50)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_money(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_empty_drinks_list(self):
        self.assertEqual(0,len(self.pub.drinks))

    def test_pub_has_drinks(self):
        self.pub.add_drink_to_pub(self.drink_1)
        self.pub.add_drink_to_pub(self.drink_2)
        self.assertEqual(2, len(self.pub.drinks))

    def test_add_money_to_till(self):
        self.pub.add_money_to_till(self.drink_2.price)
        self.assertEqual(107.50, self.pub.till)

    def test_remove_drink_from_pub(self):
        self.pub.add_drink_to_pub(self.drink_1)
        self.pub.add_drink_to_pub(self.drink_2)
        self.pub.remove_drink_from_pub(self.drink_1)
        self.assertEqual(1, len(self.pub.drinks))
    