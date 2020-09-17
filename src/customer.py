class Customer():

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.customer_drinks = []
        self.drunkenness = 0

    def remove_money_from_wallet(self, drink_price):
        self.wallet -= drink_price

    def add_drink_to_customer(self, new_drink):
        self.customer_drinks.append(new_drink)

    def buy_drink(self, drink_to_buy, drink_to_buy_price):
        self.add_drink_to_customer(drink_to_buy)
        self.remove_money_from_wallet(drink_to_buy_price)

