from players import Players


class Cauteloso(Players):
    def __init__(self):
        super().__init__()
        self.name = "Cauteloso"
        self.pos = 0
        self.properties = []
        self.lost = False
        
    def __repr__(self):
        return self.name + " " + super(Cauteloso, self).__repr__()

    def buy_property(self, prop):
        if self.budget >= prop.c_sale and (self.budget - prop.c_sale) >= 80:
            return True
        else:
            print(super().has_budget())
            print(prop.c_sale)
            return False
