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
    if (top_cash > 0):
        return random.randint(1, top_cash)
    else:
        print "You must have a max cash amount of more than 0 dollars!"
        return

def shuffle_word(word):
    string_list = list(word)
    random.shuffle(string_list)
    return "".join(string_list)

def pick_word(player_word, correct_word):
    if (player_word.lower() == correct_word.lower()):
        print "You got it right! " + player_word + " is the right word!"
        return True
    else:
        print "Sorry, " + player_word + " is not the right word"
        return False#eg: did they get it right


def end_game(player_cash):
    print "You have won $" + str(player_cash)
    print "Thank you for playing!"

def play():
    max_cash = 200
    words = init_words()
    strikes = 0;
    player_cash = 0;
    max_strikes = 4;
    while (strikes < max_strikes):
        poss_cash = spin_wheel(max_cash)
        print "You have $" + str(player_cash)
        print "You're playing for $" + str(poss_cash)
        chosen_word = words[random.randint(0, len(words) - 1)]
        print shuffle_word(chosen_word)
        player_input = raw_input('Enter your word: [RETURN to quit] ')
        if (player_input == ""):
            end_game(player_cash)
            break
        has_won = pick_word(player_input, chosen_word)
        if has_won:
            player_cash += poss_cash
        else:
            strikes += 1
            print "You got an answer wrong! You have " + str(strikes) + " strikes against you. The maximum is " + str(max_strikes) + "." 
    else :
        end_game(player_cash)

play()
