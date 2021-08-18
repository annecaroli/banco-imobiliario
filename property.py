import random


class Property:
    def __init__(self, name):
        self.name = name
        self.c_sale = random.randrange(50, 200, 10)
        self.c_rent = int(0.3 * self.c_sale)
        self.has_owner = False
        self.owner = ''

    def __repr__(self):
        return self.name + " " + str(self.c_sale) + " " + str(self.c_rent) + " " + str(self.has_owner)
