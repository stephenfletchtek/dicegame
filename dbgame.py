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
    # reuse if already connected
    db.connect(reuse_if_open=True)
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

        # end of game if all scores are assigned
        end_game = Game.select().order_by(Game.index.desc()).dicts().get()
        if len(available_scores(end_game)) == 0:
            scores = [end_game[key] for key in end_game if key != 'index']
            print(f'Final score: {sum(scores)}')
            print('Game Over! \n')
            next_action = input('New game or quit? [N/q] \n').lower().strip()
            if next_action == 'q':
                break
            else:
                initialise()
    # close the database
    db.close()

# roll the dice
# takes a rolled hand and number of rerolls
# returns a hand and rerolls = 0
def roll_dice(rolled, rerolls):
    """Roll dice."""
    if not rolled:
        rolled = YahtzeeHand()
        print(rolled)
    else:
        print('Hand already rolled: {}'.format(rolled))
    return rolled, rerolls

#re-roll the dice if they were rolled and allow 2 attempts
# takes a rolled hand and number of rerolls
# returns a new rolled hand and increments rerolls by +1
def reroll(rolled, rerolls):
    """Reroll selected dice."""
    if rolled:
        if rerolls < 2:
            #validate decision by comparing roll_list and reroll_list
            decision = input('List dice to re-roll:   ')
            # list of integers from 'decision'
            reroll_list = list(map(int, filter(str.isdigit, decision)))
            # map dice.D6 to integer for comparision
            roll_list = list(map(int, rolled))
            # check re_roll list is valid - each item must be in the original
            check_list = [
                False if reroll_list.count(item) > roll_list.count(item)
                else True for item in reroll_list
            ]
            if not False in check_list:
                rolled = YahtzeeHand(rolled, reroll_list)
                rerolls += 1
                print('New hand {}\n'.format(rolled))
            else:
                print('Bad reroll list!\n')
        else:
            print('Only 2 rerolls allowed!\n')
    else:
        print('Roll dice first\n')
    return rolled, rerolls

# score the hand and record in database if dice were rolled
# takes a rolled hand and number of rerolls
# returns an empty hand and zero rerolls if score was valid
def score_hand(rolled, rerolls):
    """Score hand."""
    if rolled:
        print('{} What shall I score?'.format(rolled))
        # get most recent game as a dict
        game_dict = Game.select().order_by(Game.index.desc()).dicts().get()
        # show items not already scored
        score_list = available_scores(game_dict)
        print(score_list)

        my_input = input('> ').lower().strip()
        if my_input in score_list:
            # convert input to database field
            input_k = [key for key in func_dict]
            db_keys = [key for key in game_dict if key != 'index']
            convert = {input_k[k]: db_keys[k] for k in range(len(input_k))}
            # determine the score
            my_score = func_dict[my_input](rolled)
            # select game
            current_game = Game.select().order_by(Game.index.desc()).get()
            # modify database
            setattr(current_game, convert[my_input], my_score)
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

# view games and scores in the database
# takes a rolled hand and number of rerolls - passes them through
def view_scores(rolled, rerolls):
    """View all games"""
    games = Game.select()
    for game in games:
        record = game.select().where(Game.index == game.index).dicts().get()
        print(f'Game: {record["index"]}')
        # substitute any '-1' scores with '-'
        my_print = [
            f'{key}:-' if record[key] == -1 else f'{key}:{record[key]}'
            for key in record
        ]
        print('  '.join(my_print[1:7]))
        print('  '.join(my_print[7:]))

        next_action = input('Next or quit? [N/q] \n').lower().strip()
        if next_action == 'q':
            break
    return rolled, rerolls

# delete all database entries
# takes a rolled hand and number of rerolls - passes them through
def delete_games(rolled, rerolls):
    """Delete all games."""
    if input('Are you sure? [y/N]').lower().strip() == 'y':
        Game.delete().execute()
        print('All games deleted! \n')
        next_action = input('New game or quit? [N/q] \n').lower().strip()
        if next_action == 'q':
            db.close()
            exit()
        else:
            initialise()
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
