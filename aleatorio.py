from players import Players
import random


class Aleatorio(Players):
    def __init__(self):
        super().__init__()
        self.name = "Aleatorio"
        self.pos = 0
        self.properties = []
        
    def __repr__(self):
        return self.name + " " + super(Aleatorio, self).__repr__()

    def buy_property(self, prop):
        if self.budget >= prop.c_sale and random.uniform(0, 1) >= 0.50:
            return True
        else:
            return False
