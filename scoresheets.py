class YahtzeeScoresheet:
    #It's all about the Yahtzee dict list hand._sets.items()

    def _score_set(self, hand, set_size):
        scores = [0]
        for dict_index, how_many in hand._sets.items():
            if how_many == set_size:
                scores.append(dict_index*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_three_kind(self, hand):
        return self._score_set(hand, 3)

    def score_four_kind(self, hand):
        return self._score_set(hand, 4)

    def score_full_house(self, hand):
        my_three = int(self.score_three_kind(hand))/3
        my_two = int(self.score_one_pair(hand))/2
        if my_three and my_two and my_three != my_two:
            return 25
        else:
            return 0

    def score_sm(self, hand):
        count = 0
        for dict_index, how_many in hand._sets.items():
            if how_many:
                count += 1
            elif dict_index > 2:
                break
        if count >= 4:
            return 30
        else:
            return 0

    def score_lg(self, hand):
        count = 0
        for dict_index, how_many in hand._sets.items():
            if how_many:
                count += 1
            elif dict_index >1:
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
        score = 0
        for dict_index, how_many in hand._sets.items():
            score += dict_index*how_many
        return score

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
