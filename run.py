import random
import re


def get_word():
    """
    Gets a random 5 letter word from the list of words
    """
    file = open("assets/words.txt", "r")
    random_word = random.choice(file.readlines()).strip("\n")
    print(random_word)
    file.close()
    return random_word


def check_word(guess_word):
    """
    Contains logic for checking if the users word
    is equal to the random word, logic needs to be added
    """
    random_word = get_word()

    if guess_word == random_word:
        print("Congratulations you win!")
    else:
        for c, w in zip(random_word, guess_word):
            if w in random_word and w in c:
                print(w + " Y ")
            elif w in random_word:
                print(w + " D ")
            else:
                print(" N ")


def check_for_special_char(user_input):
    """
    Check if the user has entered any special characters
    within their input
    """

    special_char_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if special_char_check.search(user_input) is None:
        return True
    else:
        return False


def instructions():
    """
    Instructions for the user on how to play the game
    """
    print("""Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts
Your Progress Guide "YNNYD"
"Y" Indicates that the letter at that position was guessed correctly
"D" indicates that the letter at that position is in the hidden word, but in a different position
"N" indicates that the letter at that position is wrong, and isn't in the hidden word   """)


def run_game():
    """
    Function that puts all other functions together
    forming the game.
    """
    attempts = 6
    instructions()
    print("Press [Y] to play or [Q] to quit. \n")
    play_game = input()
    try:
        if check_for_special_char(play_game) is True:
            if play_game.upper() == "Y":
                hidden_word = get_word()
                print("Enter your guess: \n")
                user_guess = input()
                try:
                    if check_for_special_char(user_guess) is True:
                        while attempts > 0:
                            check_word(user_guess)
                            attempts = attempts - 1
                except ValueError:
                    print("You entered a special character, please try again!")
    except ValueError:
        print("You entered a special character, please try again!")


run_game()
