##########################################################################
# This experiment builds upon 'game.py'                                  #
# Running 'auto.py' will roll the dice                                   #
# It will then search for the highest score it can achieve from the dice #
# This could be further developed as a 'computer' player                 #
##########################################################################
from hands import YahtzeeHand
from scoresheets import YahtzeeScoresheet

total_score = 0

score_dict = {
    '1':YahtzeeScoresheet().score_ones,
    '2':YahtzeeScoresheet().score_twos,
    '3':YahtzeeScoresheet().score_threes,
    '4':YahtzeeScoresheet().score_fours,
    '5':YahtzeeScoresheet().score_fives,
    '6':YahtzeeScoresheet().score_sixes,
    '3kind':YahtzeeScoresheet().score_three_kind,
    '4kind':YahtzeeScoresheet().score_four_kind,
    'house':YahtzeeScoresheet().score_full_house,
    'sm':YahtzeeScoresheet().score_sm,
    'lg':YahtzeeScoresheet().score_lg,
    'yahtzee':YahtzeeScoresheet().score_yahtzee,
    'chance':YahtzeeScoresheet().score_chance
}

# search available scores for highest score
while score_dict:

    # roll the dice
    y = YahtzeeHand()
    print(y)

    # try all available scores
    my_score = 0
    score_index = 0
    scores = [0],[0]

    for index, value in score_dict.items():
        scores[0].append(index)
        scores[1].append(score_dict[index](y))

    # max score and total
    score_index = scores[1].index(max(scores[1]))
    my_score = scores[1][score_index]

    total_score += my_score
    print('{}: {}'.format(scores[0][score_index], my_score))
    print('Total score: {}'.format(total_score))

    # accept?
    proceed = input('Continue or Quit?   ')

    if proceed.upper() == 'C':
        print()
        # pop scored item off the list
        if my_score != 0:
            element = score_dict.pop(scores[0][score_index])
        # pop top of list if zero score
        elif my_score == 0:
            element = score_dict.pop(next(iter(score_dict)))
    else:
        break

print('FINAL SCORE: {}'.format(total_score))
