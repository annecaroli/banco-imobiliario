import property
from property import Property


class Players:
    def __init__(self):
        self.budget = 300

    def __repr__(self):
        return str(self.budget)

    def has_budget(self):
        if self.budget > 0:
            return True
        else:
            return False
