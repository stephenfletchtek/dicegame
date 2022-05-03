from dice import D6


class Hand(list):
    #build the hand
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise VaueError('You must have a die class')
        super().__init__()

        #put the dice in a hand
        for _ in range(size):
            self.append(die_class())
        self.sort()


    #list the dice in the hand of a given value
    def _by_value(self, value):
        dice = []
        for die in self:
             if die.value == value:
                dice.append(die)
        return dice

#will make a hand of 5 dice using super() through class Hand
class YahtzeeHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    #create a dict of the sets
    def _sets(self):
        return {
            #easier than calling ones, twos etc..
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
