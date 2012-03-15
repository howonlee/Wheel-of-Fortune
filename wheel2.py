import random #this allows you to use functions in the 'random' module
#the 'random' module allows you to generate basically-random numbers

def init_words():
    words_file = open('listofwords.txt', 'r')
    for line in words_file:
    	print line
    words_file.close()
    return

def spin_wheel(top_cash):
    return

def shuffle_word(word):
    return

def pick_word(player_word, correct_word):
    return

def end_game(player_cash):
    print "You have won $" + str(player_cash)
    print "Thank you for playing!"

def play():
    init_words()#in here, we print out all the words
    player_cash = 200
    end_game(player_cash)

play()
