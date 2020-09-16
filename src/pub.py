class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = [] 

    def add_drink_to_pub(self, new_drink):
        self.drinks.append(new_drink)

    def add_money_to_till(self, drink_price):
        self.till += drink_price

    def remove_drink_from_pub(self, drink_to_remove):
        self.drinks.remove(drink_to_remove)

    def sell_drink(self, drink_to_sell):
        pass