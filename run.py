import random


def get_word():
    """
    Gets a random 5 letter word from the list of words
    """
    file = open("assets/words.txt", "r")
    word = random.choice(file.readlines()).strip("\n")
    print(word)


def check_word(str):
    """
    Contains logic for checking if the users word
    is equal to the random word, logic needs to be added
    """
    for char in str:
        if char in str:
            print("Good job!")


word = get_word()

print("Please enter a word: ")
user_word = input()
check_word(user_word)
