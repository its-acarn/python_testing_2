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

    def test_remove_money_from_wallet(self):
        self.customer.remove_money_from_wallet(self.drink_1.price)
        self.assertEqual(96.60, self.customer.wallet)