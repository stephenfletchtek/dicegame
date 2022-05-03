from hands import YahtzeeHand
from reroll import RerollHand
from scoresheets import YahtzeeScoresheet


yhand = YahtzeeHand()

func_dict = {
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

print(yhand)

for _ in range (2):
    decision = input('Score or list dice to re-roll:   ')
    if decision.upper() == 'S':
        break
    else:
        yhand = RerollHand(yhand, *decision)
        print(yhand)


try:
    my_score = func_dict[input('What shall I score?   ')](yhand)
    print(my_score)
except:
    print('Invalid score command')
    
