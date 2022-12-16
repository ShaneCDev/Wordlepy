import random
import os
import re
import colorama
from colorama import Fore, Back
import sys


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
    print(random_word)
    file.close()
    return random_word


def check_for_nums(string):
    """
    Checks if the user has entered numbers in their input
    """
    num_check = re.compile('[0-9]')

    if num_check.search(string) is None:
        return True
    else:
        print(Fore.RED + "Your choice contains numbers please try again.")
        return False


def check_for_special_char(string):
    """
    Check if the user has entered any special characters
    within their input
    """

    special_char_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if special_char_check.search(string) is None:
        return True
    else:
        spec_msg = "Your choice contains special characters please try again."
        print(Fore.RED + spec_msg)
        return False


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


def is_empty(string):
    """
    Function to check if a user string is empty or not.
    """
    if not string and string.strip():
        return True
    else:
        print(Fore.RED + "You did not enter a character please try again.\n")
        return False


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
    

def data_validation(string):
    """
    Function that completes all data validation
    """
    data_validated = False
    while not data_validated:
        if is_empty(string) is False:
            print(Fore.RED + "You did not enter a character please try again.")
            continue
        elif check_for_nums(string) and check_for_special_char(string) is False:
            print(Fore.RED + "You choice contains special characters and/or numbers please try again.\n")
        else:
            data_validated = True
    return True


def instructions():
    """
    Instructions for the user on how to play the game
    """
    print(Fore.GREEN + """Wordle is a single player game:
    A player has to guess a five letter hidden word.
    You have six attempts to guess the word!
    Your progress guide:
    A green background means the letter is in the correct place.
    A yellow background means the letter is in the word but in the wrong place.
    A red background means that, that letter does not appear in the word.\n
    """)

    print(Fore.GREEN + "Would you like to play? [Y] or [N] \n")
    play_yes_no = input()
    if data_validation(play_yes_no) is True:
        if play_yes_no.upper() == "Y":
            clear_screen()
            game_logic(0)
        else:
            print(Fore.GREEN + "Maybe next time!")
            sys.exit()


def new_run_game():
    """
    Function that puts all functions together to run the game.
    """
    main_menu()
    while True:
        choice = input()
        if choice == "1":
            game_logic(0)
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


def game_logic(attempts):
    """
    Logic for the game itself.
    """
    random_word = get_word()
    len_of_guess = True
    turns = 6
    random_word.upper()
    print("The word is: " + random_word.upper())
    while attempts < 6:
        print(f'{Fore.GREEN}You have {turns} attempts left!')
        turns = turns - 1
        user_guess = input("Enter your guess: \n")
        if check_for_special_char(user_guess) is False:
            print("Your guess contains special characters, please try again!")
        if len(user_guess) != len(random_word):
            len_too_short = f'{Fore.RED}You entered a word with ' \
                f'{len(user_guess)} characters,  please try again and' \
                f' enter a word with {len(random_word)} characters!'
            print(len_too_short)
            len_of_guess = False
        while not len_of_guess:
            user_guess = input(Fore.GREEN + "Enter another guess: ")
            if len(user_guess) == len(random_word):
                len_of_guess = True
        for i in range(len(random_word)):
            if user_guess == random_word:
                congrats = f'{Fore.GREEN}Congratulations you guessed' \
                    f' the word in {attempts + 1} attempts'
                clear_screen()
                you_win()
                print(congrats)
                play_again = input("Would you like to play again? [Y] or [N]: ")
                print(play_again)
                if (check_for_special_char(play_again) 
                   and check_for_nums(play_again) is False):
                    ans = "Your answer contains special characters please try again.\n"
                    print(Fore.RED + ans)
            if user_guess[i] == random_word[i]:
                print(f'{Back.GREEN}{Fore.BLACK}{user_guess[i].upper()}',
                      end="")
            elif (user_guess[i] in random_word 
                    and user_guess.count(user_guess[i]) 
                    <= random_word.count(user_guess[i])):
                print(f'{Back.YELLOW}{Fore.BLACK}{user_guess[i].upper()}',
                      end="")
            else:
                print(Back.RED + "_", end="")
        attempts += 1
        if attempts == 6:
            clear_screen()
            lost = "\nSorry, you didn't guess the word, better luck next time!"
            you_lose()
            print(Fore.RED + lost)


new_run_game()