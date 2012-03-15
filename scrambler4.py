import random #this allows you to use functions in the 'random' module
#the 'random' module allows you to generate basically-random numbers

def init_words():
    words = []
    words_file = open('listofwords.txt', 'r')
    for line in words_file:
        words.append(line.strip())
    words_file.close()
    return words

def spin_wheel(top_cash):
    return

def shuffle_word(word):
    return

def pick_word(player_word, correct_word):
    if (player_word.lower() == correct_word.lower()):
        print "You got it right! " + player_word + " is the right word!"
        return True
    else:
        print "Sorry, " + player_word + " is not the right word"
        return False


def end_game(player_cash):
    print "You have won $" + str(player_cash)
    print "Thank you for playing!"

def play():
    words = init_words()
    strikes = 0;
    player_cash = 0;
    while (strikes < 4):
        print "You have $" + str(player_cash)
        print "You're playing for $50"
        chosen_word = words[random.randint(0, len(words) - 1)]
        print chosen_word
        player_input = raw_input('Enter your word: [RETURN to quit] ')
        if (player_input == ""):
            end_game(player_cash)
            break
        has_won = pick_word(player_input, chosen_word)
        if has_won:
            player_cash += 50
        else:
            strikes += 1
    else :
        end_game(player_cash)

play()
