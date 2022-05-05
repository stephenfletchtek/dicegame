###############################################################
# These unit tests check score behaviour in 'scoresheeets.py' #
###############################################################
import unittest

import dice, hands, scoresheets


# test properties of Die
class DieTests(unittest.TestCase):
    def setUp(self):
        # make 8 hands to test scoring
        self.hand = []
        for _ in range(9):
            self.hand.append(hands.YahtzeeHand())

        for index in range(9):
            for item in range(5):
                # ones to sixes
                if index < 6:
                    self.hand[index][item].value = index + 1
                # [6] is full house, [7] is small straight, [8] is lge straight
                elif index == 6 or index == 7:
                    if item < 2:
                        self.hand[index][item].value = 2
                    else:
                        self.hand[6][item].value = 3
                        self.hand[7][item].value = item + 1
                else:
                    self.hand[index][item].value = item + 1

    def test_creation(self):
        for index in range(9):
            self.assertIsInstance(self.hand[index], hands.Hand)
            self.assertEqual(len(self.hand[index]), 5)

    def test_eq(self):
        # check each hand scores as anticipated
        # instantiate object
        score_obj = scoresheets.YahtzeeScoresheet()
        # the expected scores for each hand
        scores = [
            {'function':score_obj.score_ones(self.hand[0]), 'score':5},
            {'function':score_obj.score_ones(self.hand[1]), 'score':0},
            {'function':score_obj.score_twos(self.hand[1]), 'score':10},
            {'function':score_obj.score_twos(self.hand[2]), 'score':0},
            {'function':score_obj.score_threes(self.hand[2]), 'score':15},
            {'function':score_obj.score_threes(self.hand[3]), 'score':0},
            {'function':score_obj.score_fours(self.hand[3]), 'score':20},
            {'function':score_obj.score_fours(self.hand[4]), 'score':0},
            {'function':score_obj.score_fives(self.hand[4]), 'score':25},
            {'function':score_obj.score_fives(self.hand[5]), 'score':0},
            {'function':score_obj.score_sixes(self.hand[5]), 'score':30},
            {'function':score_obj.score_sixes(self.hand[0]), 'score':0},
            {'function':score_obj.score_three_kind(self.hand[5]), 'score':18},
            {'function':score_obj.score_three_kind(self.hand[7]), 'score':0},
            {'function':score_obj.score_four_kind(self.hand[4]), 'score':20},
            {'function':score_obj.score_four_kind(self.hand[6]), 'score':0},
            # {'function':score_obj.score_full_house(self.hand[6]), 'score':25},
            {'function':score_obj.score_full_house(self.hand[0]), 'score':0},
            {'function':score_obj.score_sm(self.hand[7]), 'score':30},
            {'function':score_obj.score_sm(self.hand[8]), 'score':30},
            {'function':score_obj.score_sm(self.hand[0]), 'score':0},
            {'function':score_obj.score_lg(self.hand[8]), 'score':40},
            {'function':score_obj.score_lg(self.hand[7]), 'score':0},
            {'function':score_obj.score_yahtzee(self.hand[5]), 'score':50},
            {'function':score_obj.score_yahtzee(self.hand[6]), 'score':0},
            {'function':score_obj.score_chance(self.hand[6]), 'score':13},
            {'function':score_obj.score_chance(self.hand[5]), 'score':30}
        ]
        # loop through each test
        for item in scores:
            self.assertEqual(item['function'], item['score'])

if __name__ == '__main__':
    unittest.main()
