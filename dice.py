########################################
# python tutorial to make a die object #
# and then a D6 based on die object    #
# Code based on tutorial               #
########################################
import random


# Die object
class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError('Must have at least 2 sides')
        if not isinstance(sides, int):
            raise ValueError('Must have a whole number of sides')
        self.value = value or random.randint(1, sides)
        # sides attribute was not visible and failed tests
        self.sides = sides

    def __int__(self):
        return int(self.value)

    # this was typoed as def __eq_ and picked up on test
    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


# make a D6
class D6(Die):
    def __init__(self, value = 0):
        super().__init__(sides=6, value = value)
