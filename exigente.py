from players import Players


class Exigente(Players):
    def __init__(self):
        super().__init__()
        self.name = "Exigente"
        self.pos = 0
        self.properties = []
        self.lost = False
        
    def __repr__(self):
        return self.name + " " + super(Exigente, self).__repr__()

    def buy_property(self, prop):
        if self.budget >= prop.c_sale and prop.c_rent >= 50:
            return True
        else:
            return False
