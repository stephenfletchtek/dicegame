############################################################
# I added the capability to reroll part or all of the hand #
############################################################
from dice import D6


# the modifiable hand takes a reroll_list of those dice to reroll
class Modhand(list):
    # build the hand
    def __init__(self, hand, *reroll_list, size=0, die_class=None, **kwargs):
        if not die_class:
            raise VaueError('You must have a die class')

        # modify the hand by inserting new dice
        # over existing numbers specified in reroll_list
        try:
            for element in reroll_list:
                hand = list(map(int, hand))
                hand[hand.index(int(element))] = die_class()
        except:
            # handle an empty list
            print('Invalid reroll list')
        finally:
            # put the dice into the Modhand object
            for item in hand:
                self.append(item)
                self.sort()

    # list the dice in the hand of a given value
    def _by_value(self, value):
        dice = []
        for die in self:
            # no need for 'int(die)'
            if die == value:
                dice.append(die)
        return dice

# will make a hand of 5 dice using super() through class Hand
class RerollHand(Modhand):
    def __init__(self, hand, *reroll_list, **kwargs):
        super().__init__(hand, *reroll_list, size=5, die_class=D6, **kwargs)


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
    # create a dict of the sets
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
