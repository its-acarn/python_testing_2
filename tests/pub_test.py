import unittest
from src.pub import Pub 

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("Ox", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_money(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_empty_drinks_list(self):
        self.assertEqual(0,len(self.pub.drinks))