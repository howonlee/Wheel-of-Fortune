import random #this allows you to use functions in the 'random' module
#the 'random' module allows you to generate basically-random numbers

def init_words():
    words = []
    with open("listofwords.txt") as file:
        for line in file:
            words.append(line)

def spin_wheel(top_cash):
    if (top_cash > 0):
        return randint(1, top_cash)
    else:
        print "You must have a max cash amount of more than 0 dollars!"
        return

def pick_word(player_word, correct_word):
    if (lower(player_word) == lower(correct_word)):
        print "You got it right! " + player_word + " is the right word!"
        return True
    else:
        print "Sorry, " + player_word + " is not the right word"
        return False#eg: did they get it right

def play():
    max_cash = 200
    words = init_words()
    chosen_word = words[randint(0, len(words) - 1)]
    strikes = 0;
    while (strikes < 4):
        spin_wheel(max_cash)
        player_input = raw_input('Enter your word: ')
        pick_word(player_input, chosen_word)
