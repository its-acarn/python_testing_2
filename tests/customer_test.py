import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Harrison", 100.00)

    def test_customer_has_a_name(self):
        self.assertEqual("Harrison", self.customer.name)

    