import random

ALLOWED_ATTEMPTS = 6


def get_word():
    """
    Gets a random 5 letter word from the list of words
    """
    file = open("assets/words.txt", "r")
    random_word = random.choice(file.readlines()).strip("\n")
    print(random_word)
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


word = get_word()

print("Please enter a word: ")
user_word = input()
check_word(user_word)
