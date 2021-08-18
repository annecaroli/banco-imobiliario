from players import Players


class Impulsivo(Players):
    def __init__(self):
        super().__init__()
        self.name = "Impulsivo"
        self.pos = 0
        self.properties = []
        self.lost = False

    def __repr__(self):
        return self.name + " " + super(Impulsivo, self).__repr__()

    def buy_property(self, prop):
        if self.budget >= prop.c_sale:
            return True
        else:
            return False
