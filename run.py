import random
import re
import colorama
from colorama import init, Fore, Back, Style

colorama.init(autoreset=True)

def get_word():
    """
    Gets a random 5 letter word from the list of words
    """
    file = open("assets/words.txt", "r", encoding="utf-8")
    random_word = random.choice(file.readlines()).strip("\n")
    print(random_word)
    file.close()
    return random_word

"""
def check_word(guess_word):
    """
    #Contains logic for checking if the users word
    #is equal to the random word, logic needs to be added
"""
    random_word = get_word()

    if guess_word == random_word:
        print("Congratulations you win!")
    else:
        for c, w in zip(random_word, guess_word):
            if w in random_word and w in c:
                print(w + str(curses.COLOR_GREEN))
            elif w in random_word:
                print(w + str(curses.COLOR_YELLOW))
            else:
                print(str(curses.COLOR_RED))
"""


def check_for_special_char(string):
    """
    Check if the user has entered any special characters
    within their input
    """

    special_char_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if special_char_check.search(string) is None:
        return True
    else:
        return False


def instructions():
    """
    Instructions for the user on how to play the game
    """
    print(r" __      __                .___.__        __________        ")
    print(r"/  \    /  \___________  __| _/|  |   ____\______   \___.__.")
    print(r"\   \/\/   /  _ \_  __ \/ __ | |  | _/ __ \|     ___<   |  |")
    print(r" \        (  <_> )  | \/ /_/ | |  |_\  ___/|    |    \___  |")
    print(r"  \__/\  / \____/|__|  \____ | |____/\___  >____|    / ____|")
    print(r"       \/                   \/           \/          \/     ")

    print("""Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts
Your Progress Guide "YNNYD"
"Y" Indicates that the letter at that position was guessed correctly
"D" indicates that the letter at that position is in the hidden word, but in a different position
"N" indicates that the letter at that position is wrong, and isn't in the hidden word   """)

"""
def run_game():
    """
    #Function that puts all other functions together
    #forming the game.
"""
    attempts = 6
    instructions()
    print("Press [Y] to play or [Q] to quit. \n")
    play_game = input()
    try:
        if check_for_special_char(play_game) is True:
            if play_game.upper() == "Y":
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
"""


def new_run_game():
    instructions()
    print("Press [Y] to play or [Q] to quit. \n")
    user_choice = input()
    if check_for_special_char(user_choice) is True:
        if user_choice.upper() == "Y":
            game_logic(0)


def game_logic(attempts):
    random_word = get_word()
    len_of_guess = True
    turns = 6
    random_word.upper()
    print("The word is: " + random_word.upper())
    #output = ""
    while attempts < 6:
        print(f'You have {turns} attempts left!')
        turns = turns - 1
        user_guess = input("Enter your guess: \n")
        if check_for_special_char(user_guess) is False:
            print("Your guess contains special characters, please try again!")
        if len(user_guess) != len(random_word):
            print(f'You entered a word with {len(user_guess)} characters, please try again and enter a word with {len(random_word)} characters!')
            len_of_guess = False
        while not len_of_guess:
            user_guess = input("Enter another guess: ")
            if len(user_guess) == len(random_word):
                len_of_guess = True
        for i in range(len(random_word)):
            if user_guess == random_word:
                print(f'Congratulations you guessed the word in {attempts} attempts!')
                return
            if user_guess[i] == random_word[i]:
                print(f'{Back.GREEN}{user_guess[i]}', end="")
            elif user_guess[i] in random_word and user_guess.count(user_guess[i]) <= random_word.count(user_guess[i]):
                print(user_guess[i].upper(), end="")
            else:
                print("_", end="")
        attempts += 1
        if attempts == 6:
            print("\nSorry, you didn't guess the word, better luck next time!")
        print("")


new_run_game()