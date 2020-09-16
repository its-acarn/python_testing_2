class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = [] 

    def add_drink_to_pub(self, new_drink):
        self.drinks.append(new_drink)

    