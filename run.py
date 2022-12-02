import random

ALLOWED_ATTEMPTS = 6


def get_word():
    """
    Gets a random 5 letter word from the list of words
    """
    file = open("assets/words.txt", "r")
    random_word = random.choice(file.readlines()).strip("\n")
    print(random_word)


def check_word(word):
    """
    Contains logic for checking if the users word
    is equal to the random word, logic needs to be added
    """
    for char in word:
        if char in word:
            print("Good job!")


word = get_word()

print("Please enter a word: ")
user_word = input()
check_word(user_word)
