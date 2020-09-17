import unittest
from src.pub import Pub 
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Duke's Corner", 100.00)
        self.drink_1 = Drink("Tennents", 3.40)
        self.drink_2 = Drink("Wine", 7.50)
        self.customer_1 = Customer("Harrison", 22, 10.00)

        self.pub.add_drink_to_pub(self.drink_1)
        self.pub.add_drink_to_pub(self.drink_2)

    def test_pub_has_name(self):
        self.assertEqual("Duke's Corner", self.pub.name)

    def test_pub_has_money(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks_list(self):
        self.assertEqual(type([]),type(self.pub.drinks))

    def test_pub_has_drinks(self):
        # self.pub.add_drink_to_pub(self.drink_1)
        # self.pub.add_drink_to_pub(self.drink_2)
        self.assertEqual(2, len(self.pub.drinks))

    def test_add_money_to_till(self):
        self.pub.add_money_to_till(self.drink_2.price)
        self.assertEqual(107.50, self.pub.till)

    def test_remove_drink_from_pub(self):
        # self.pub.add_drink_to_pub(self.drink_1)
        # self.pub.add_drink_to_pub(self.drink_2)
        self.pub.remove_drink_from_pub(self.drink_1)
        self.assertEqual(1, len(self.pub.drinks))
    
    def test_sell_drink(self):
        # self.pub.add_drink_to_pub(self.drink_1)
        # self.pub.add_drink_to_pub(self.drink_2)
        self.pub.sell_drink(self.drink_1, self.drink_1.price)
        self.assertEqual(1, len(self.pub.drinks))
        self.assertEqual(103.40, self.pub.till)
    
    def test_age_check(self):
        result = self.pub.age_check(self.customer_1.age)
        self.assertEqual("OK to serve", result)