#############################################################
# python tutorial to make a 'hand' of die objects           #
# and then a yahtzeehand of 5 dice based on the Hand object #
# Code based on tutorial                                    #
#############################################################
from dice import D6

# a hand of dice
class Hand(list):
    def __init__(self, hand=None, reroll_list=None, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise VaueError('You must have a die class')
        super().__init__()
        # reroll if arguments were passed
        if hand and reroll_list:
            for item in reroll_list:
                # this swaps out the first one it finds, and not all of them!
                hand[hand.index(item)] = die_class()
            [self.append(item) for item in hand]
        # else make a new hand of 5 dice
        else:
            [self.append(die_class()) for _ in range(size)]
        self.sort()

    # list the dice in the hand of a given value
    def _by_value(self, value):
        return [die for die in self if die == value]

# makes a hand of 5 random dice if 'hand' and 'reroll_list' are blank
# if 'hand' if duce.D6 and a 'reroll_list' of values are given
# it rerolls dice in the hand matching the reroll list
class YahtzeeHand(Hand):
    def __init__(self, hand=None, reroll_list=None, *args, **kwargs):
        super().__init__(hand, reroll_list, size=5, die_class=D6, *args, **kwargs)

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
