########################################################################
# The turorial did not have this file - it simply rolled one hand      #
# and alowed it to be scored                                           #
# I connected a database and made this a solo player game based on the #
# UK version of Yahtzee                                                #
# It is a simple user interface through command line / terminal prompt #
########################################################################
from collections import OrderedDict
from peewee import *
from hands import YahtzeeHand
from reroll import RerollHand
from scoresheets import YahtzeeScoresheet

db = SqliteDatabase('yahtzee.db')


class Game(Model):
    index = IntegerField(primary_key=True)
    aces = IntegerField(default='-1')
    twos = IntegerField(default='-1')
    threes = IntegerField(default='-1')
    fours = IntegerField(default='-1')
    fives = IntegerField(default='-1')
    sixes = IntegerField(default='-1')
    three_kind = IntegerField(default='-1')
    four_kind = IntegerField(default='-1')
    house = IntegerField(default='-1')
    sm =  IntegerField(default='-1')
    lg = IntegerField(default='-1')
    yahtzee = IntegerField(default='-1')
    chance = IntegerField(default='-1')

    class Meta:
        database = db


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

# create a new game
def initialise():
    db.connect()
    # create table if it doesn't already exist
    db.create_tables([Game],safe=True)
    # create a new game
    Game.create()

# main menu loop
def menu_loop():
    """Main menu."""
    choice = None
    rolled = None
    rerolls = 0

    while choice !='q':
        print("Main menu: Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('> ').lower().strip()

        if choice in menu:
            result = menu[choice](rolled, rerolls)
            rolled = result[0]
            rerolls = result[1]
    # close the database
    db.close()

# roll the dice
def roll_dice(rolled, rerolls):
    """Roll dice."""
    if not rolled:
        rolled = YahtzeeHand()
        print(rolled)
    else:
        print('Hand already rolled: {}'.format(rolled))

    return rolled, rerolls

#re-roll the dice if they were rolled and allow 2 attempts
def reroll(rolled, rerolls):
    """Reroll selected dice."""
    if rolled:
        if rerolls < 2:
            decision = input('List dice to re-roll:   ')

            #validate decision by comparing roll_list and reroll_list
            #strip out non numeric characters so any input will work!
            stripped_decision = filter(str.isdigit, decision)
            reroll_list = list(map(int, stripped_decision))
            roll_list = list(map(int, rolled))

            match = False
            for item in reroll_list:
                if reroll_list.count(item) > roll_list.count(item):
                    match = False
                    break
                else:
                    match = True

            #if list is valid
            if match:
                rolled = RerollHand(rolled, *reroll_list)
                rerolls += 1
                print('New hand {}\n'.format(rolled))
            else:
                print('Bad reroll list!\n')
        else:
            print('Only 2 rerolls allowed!\n')
    else:
        print('Roll dice first\n')
    return rolled, rerolls

# score the hand if dice were rolled
def score_hand(rolled, rerolls):
    """Score hand."""
    if rolled:
        print('{} What shall I score?'.format(rolled))
        # get most recent game as a dict
        game_dict = Game.select().order_by(Game.index.desc()).dicts().get()
        #show items not already scored
        score_list = available_scores(game_dict)
        print(score_list)

        my_input = input('> ').lower().strip()
        if my_input in score_list:
            my_score = func_dict[my_input](rolled)
            current_game = Game.select().order_by(Game.index.desc()).get()

            if my_input == '1': current_game.aces = my_score
            if my_input == '2': current_game.twos = my_score
            if my_input == '3': current_game.threes = my_score
            if my_input == '4': current_game.fours = my_score
            if my_input == '5': current_game.fives = my_score
            if my_input == '6': current_game.sixes = my_score
            if my_input == '3kind': current_game.three_kind = my_score
            if my_input == '4kind': current_game.four_kind = my_score
            if my_input == 'house': current_game.house = my_score
            if my_input == 'sm': current_game.sm = my_score
            if my_input == 'lg': current_game.lg = my_score
            if my_input == 'yahtzee': current_game.yahtzee = my_score
            if my_input == 'chance': current_game.chance = my_score

            current_game.save()
            print('Score: {} saved!\n'.format(my_score))

            #reset game after scoring
            rerolls = 0
            rolled = None

        else:
            print('"{}" is not in the list.\n'.format(my_input))
    else:
        print('Roll dice first\n')
    return rolled, rerolls

def view_scores(rolled, rerolls):
    """View previous games"""
    games = Game.select()

    for game in games:
        record = game.select().where(Game.index == game.index).dicts().get()
        game_num = record.pop('index')
        print('Game: {}'.format(game_num))

        my_print = []
        for key in record.keys():
            #turn -1 into '-' for display
            if record[key] == -1:
                record[key] = "-"
            data = '{}:{}'.format(key, record[key])
            my_print.append(data)

        separator = '  '
        print(separator.join(my_print[:6]))
        print(separator.join(my_print[6:]))

        next_action = input('Action [N/q] \n').lower().strip()
        if next_action =='q':
            break
    return rolled, rerolls

def delete_games(rolled, rerolls):
    """Delete all games."""
    if input('Are you sure? [y/N]').lower().strip() == 'y':
        Game.delete().execute()
        # close the database
        db.close()
        initialise()
        print('All games deleted!')
    return rolled, rerolls

# takes a dict of the (current) game to check scores against
# returns a list of 'func_dict' keys where database score is '-1'
def available_scores(game):
    # list of database keys in 'game' but not 'index'
    in_db = [key for key in game if key != 'index']
    # list of keys to display for scoring
    to_score = [key for key in func_dict]
    # give 'to score' key if value of game key is '-1'
    return [to_score[i] for i in range(len(to_score)) if game[in_db[i]] == -1]

menu = OrderedDict([
        ('r', roll_dice),
        ('e', reroll),
        ('s', score_hand),
        ('v', view_scores),
        ('d', delete_games)
    ])

if __name__ == '__main__':
    initialise()
    menu_loop()
