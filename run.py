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


def logo():
    """
    Ascii art logo
    """
    print(Fore.YELLOW + r" __      __                .___.__        __________        ")
    print(Fore.YELLOW + r"/  \    /  \___________  __| _/|  |   ____\______   \___.__.")
    print(Fore.YELLOW + r"\   \/\/   /  _ \_  __ \/ __ | |  | _/ __ \|     ___<   |  |")
    print(Fore.YELLOW + r" \        (  <_> )  | \/ /_/ | |  |_\  ___/|    |    \___  |")
    print(Fore.YELLOW + r"  \__/\  / \____/|__|  \____ | |____/\___  >____|    / ____|")
    print(Fore.YELLOW + r"       \/                   \/           \/          \/     ")


def instructions():
    """
    Instructions for the user on how to play the game
    """
    print("""Wordle is a single player game
    A player has to guess a five letter hidden word.
    You have six attempts to guess the word!
    Your progress guide:
    A letter with a green background indicates the letter is in the correct position.
    A letter with a yellow background indicates the letter is in the word but in the wrong position.
    A letter with a red background indicates that, that letter does not appear in the word.
    """)


def new_run_game():
    main_menu()
    choice = input()
    if int(choice) == 1:
        game_logic(0)
    elif int(choice) == 2:
        clear_screen()
        instructions()
    elif int(choice) == 3:
        print("Goodbye!")
        sys.exit()
    else:
        clear_screen()
        print(f'{Fore.RED}{choice} is not a valid option.')


def game_logic(attempts):
    random_word = get_word()
    len_of_guess = True
    turns = 6
    random_word.upper()
    print("The word is: " + random_word.upper())
    while attempts < 6:
        print(f'You have {turns} attempts left!')
        turns = turns - 1
        user_guess = input("Enter your guess: \n")
        if check_for_special_char(user_guess) is False:
            print("Your guess contains special characters, please try again!")
        if len(user_guess) != len(random_word):
            print(f'You entered a word with {Back.RED}{len(user_guess)} characters, please try again and enter a word with {len(random_word)} characters!')
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
                print(f'{Back.GREEN}{Fore.BLACK}{user_guess[i]}', end="")
            elif user_guess[i] in random_word and user_guess.count(user_guess[i]) <= random_word.count(user_guess[i]):
                print(user_guess[i].upper(), end="")
            else:
                print("_", end="")
        attempts += 1
        if attempts == 6:
            print("\nSorry, you didn't guess the word, better luck next time!")
        print("")


new_run_game()