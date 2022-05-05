#######################################################################
# The tutorial gave the 1st 14 lines of code and asked the student to #
# complete the rest.                                                  #
# I aligned the scoring to closely match the UK version of 'Yahtzee'  #
#######################################################################
class YahtzeeScoresheet:
    # It's all about the hand._sets dict
    def _score_set(self, hand, set_size):
        scores = [0]
        for key, value in hand._sets.items():
            if value >= set_size:
                scores.append(key*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_three_kind(self, hand):
        return self._score_set(hand, 3)

    def score_four_kind(self, hand):
        return self._score_set(hand, 4)

    # full house is 3 of a kind and 2 of a kind
    def score_full_house(self, hand):
        for key, value in hand._sets.items():
            # 3 of a kind
            if value == 3:
                for key, value in hand._sets.items():
                    # 2 of a kind
                    if value == 2:
                        return 25
        return 0

    # small straight is 4 in a row
    def score_sm(self, hand):
        count = 0
        for key, value in hand._sets.items():
            if value:
                count += 1
            elif key > 2:
                break
        if count >= 4:
            return 30
        else:
            return 0

    def score_lg(self, hand):
        count = 0
        for key, value in hand._sets.items():
            if value:
                count += 1
            elif key > 1:
                break
        if count == 5:
            return 40
        else:
            return 0

    def score_yahtzee(self, hand):
        if self._score_set(hand, 5) != 0:
            return 50
        else:
            return 0

    def score_chance(self, hand):
        scores = [key * hand._sets[key] for key in hand._sets]
        return sum(scores)

    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)
