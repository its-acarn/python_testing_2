import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Harrison", 100.00)
        self.drink_1 = Drink("Tennents", 3.40)
        self.drink_2 = Drink("Wine", 7.50)

    def test_customer_has_a_name(self):
        self.assertEqual("Harrison", self.customer.name)

    def test_customer_has_money_in_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)

    def test_customer_has_empty_drink_list(self):
        self.assertEqual(0, len(self.customer.customer_drinks))

    def test_remove_money_from_wallet(self):
        self.customer.remove_money_from_wallet(self.drink_1.price)
        self.assertEqual(96.60, self.customer.wallet)

    def test_add_drink_to_customer(self):
        self.customer.add_drink_to_customer(self.drink_1)
        self.assertEqual(1, len(self.customer.customer_drinks))

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink_2, self.drink_2.price)
        self.assertEqual(1, len(self.customer.customer_drinks))
        self.assertEqual(92.50, self.customer.wallet)