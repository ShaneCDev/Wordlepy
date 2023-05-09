import random
import os
import re
import sys
import colorama
from colorama import Fore, Back


colorama.init(autoreset=True)


def clear_screen():
    """
    Clears the screen so things dont get too messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_word():
    """
    Gets a random 5 letter word from the list of words
    """
    file = open("assets/words.txt", "r", encoding="utf-8")
    random_word = random.choice(file.readlines()).strip("\n")
    file.close()
    return random_word


# def check_for_nums(string):
#     """
#     Checks if the user has entered numbers in their input
#     """
#     num_check = re.compile('[0-9]')

#     if num_check.search(string) is None:
#         return True
#     else:
#         return False


# def check_for_special_char(string):
#     """
#     Check if the user has entered any special characters
#     within their input
#     """

#     special_char_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

#     if special_char_check.search(string) is None:
#         return True
#     else:
#         return False


def main_menu():
    """
    Menu to start the game, read the rules or exit the game
    """
    logo()
    print(Fore.LIGHTGREEN_EX + """
    1. Play game
    2. Read the rules
    3. Exit the game
        """)


# def is_empty(string):
#     """
#     Function to check if a user string is empty or not.
#     """
#     if string and string.strip():
#         return False
#     else:
#         return True


def you_win():
    """
    Ascii art you win text
    """
    print(Fore.GREEN + r"""
    _____.___.              __      __.__
    \__ |   | ____  __ __  /  \    /  \__| ____
    /   |   |/  _ \|  |  \ \   \/\/   /  |/    \
    \____   (  <_> )  |  /  \        /|  |   |  \
    / ______|\____/|____/    \__/\  / |__|___|  /
    \/                            \/          \/
    """)


def you_lose():
    """
    Ascii art
    """
    print(Fore.RED + r"""
    _____.___.              .__
    \__  |   | ____  __ __  |  |   ____  ______ ____
     /   |   |/  _ \|  |  \ |  |  /  _ \/  ___// __ \
     \____   (  <_> )  |  / |  |_(  <_> )___ \\  ___/
     / ______|\____/|____/  |____/\____/____  >\___  >
     \/                                     \/     \/
    """)


def goodbye():
    """
    Ascii art
    """
    clear_screen()
    print(Fore.RED + r"""
      ________                  .______.
     /  _____/  ____   ____   __| _/\_ |__ ___.__. ____
    /   \  ___ /  _ \ /  _ \ / __ |  | __ <   |  |/ __ \
    \    \_\  (  <_> |  <_> ) /_/ |  | \_\ \___  \  ___/
     \______  /\____/ \____/\____ |  |___  / ____|\___  >
            \/                   \/      \/\/         \/
    """)


def logo():
    """
    Ascii art logo
    """
    print(Fore.YELLOW + r"""
     __      __                .___.__        __________
    /  \    /  \___________  __| _/|  |   ____\______   \___.__.
    \   \/\/   /  _ \_  __ \/ __ | |  | _/ __ \|     ___<   |  |
     \        (  <_> )  | \/ /_/ | |  |_\  ___/|    |    \___  |
      \__/\  / \____/|__|  \____ | |____/\___  >____|    / ____|
           \/                   \/           \/          \/
    """)

def new_run_game():
    """
    Function that puts all functions together to run the game.
    """
    main_menu()
    while True:
        choice = input()
        if choice == "1":
            clear_screen()
            game_logic()
        elif choice == "2":
            clear_screen()
            instructions()
        elif choice == "3":
            clear_screen()
            goodbye()
            sys.exit()
        else:
            clear_screen()
            print(f'{Fore.RED}{choice} is not a valid option.')


def instructions():
    """
    Instructions for the user on how to the play the game
    """
    # print(Fore.GREEN + """Wordle is a single player game:
    # A player has to guess a hidden five letter word.
    # You have six attempts to guess the word!
    # Your progress guide:
    # A green background means the letter is in the correct place.
    # A yellow background means the letter is in the word but in the wrong place
    # A red background means that, the letter does not appear in the word.""")

    intro = Fore.GREEN + """Wordle is a single player game:
    A player has to guess a hidden five letter word.
    You have 6 attempts to guess the word!
    """

    progress_guide = f'Your progress guide:\n{Fore.GREEN}A green background means the letter is in the correct place.\n' \
    f'{Fore.YELLOW}A yellow background means the letter appears in the word but it is in the wrong place.\n' \
    f'{Fore.RED}A red background means that, the letter does not appear in the word.\n'

    print(intro + progress_guide)

    while True:
        play_yes_no = input(Fore.GREEN + "Would you like to play? [Y] or [N]: ")
        if not play_yes_no:
            print(Fore.RED + "You did not enter a character. Please try again!")
            continue
        if any(char.isdigit() or not char.isalnum() for char in play_yes_no):
            print(Fore.RED + "Sorry, your choice contains special characters please try again!")
            continue
        if play_yes_no.upper() == "Y":
            clear_screen()
            game_logic()
        elif play_yes_no.upper() == "N":
            goodbye()
            sys.exit()
        else:
            print(f'{Fore.RED}Invalid input. Please enter either Y or N.')


def validate_guess(guess, word):
    """
    Validates the users guess and returns an error message if the guess is not valid
    """
    if guess == "" or guess == " ":
        return "Your answer is blank, enter a word and try again!"
    if not guess.isalpha():
        return "Your answer contains special characters and/or numbers please try again!"
    if len(guess) != len(word):
        return f'You entered a word with {len(guess)} characters. Please try again!'


def display_correct_guesses(guess, word):
    """
    Displays which letters were guessed correctly and which were not
    """
    correct_guesses = ""
    for i, letter in enumerate(guess):
        if letter == word[i]:
            correct_guesses += Fore.GREEN + letter.upper() + " "
        elif letter in word:
            correct_guesses += Fore.YELLOW + letter.upper() + " "
        else:
            correct_guesses += Fore.RED + "_" + " "
    print(correct_guesses)

def play_again():
    """
    Asks the user if they want to play again or quit and handles the users response
    """
    while True:
        choice = input(Fore.GREEN + "Press 1 to play again or 2 to quit. [1] or [2]: ")
        if choice == "1":
            clear_screen()
            new_run_game()
        elif choice == "2":
            clear_screen()
            goodbye()
            sys.exit()
        else:
            print(f'{choice} is not a valid option.')

def game_logic():
    """
    Logic for the game itself
    """
    random_word = get_word()
    random_word.upper()
    print(random_word)
    turns = 6
    attempts = 0

    while turns > 0:
        print(f'\n{Fore.GREEN}You have {turns} guesses left!')
        user_guess = input(Fore.GREEN + "Enter your guess: ")
        validation_error = validate_guess(user_guess, random_word)
        if validation_error:
            print(Fore.RED + validation_error)
            continue

        display_correct_guesses(user_guess, random_word)

        if user_guess == random_word:
            win = f'{Fore.GREEN}Congratulations, you guessed the word in {attempts+1} attempts!'
            clear_screen()
            print(win)
            you_win()
            play_again()

        turns -= 1
        attempts += 1

    clear_screen()
    lost = "\nSorry, you didn't guess the word. Better luck next time!"
    you_lose()
    print(Fore.RED + "The word was " + random_word)
    print(Fore.RED + lost)
    play_again()



new_run_game()
