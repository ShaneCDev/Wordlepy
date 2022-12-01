import random


def get_word():
    file = open("assets/words.txt", "r")
    word = random.choice(file.readlines()).strip("\n")
    print(word)


get_word()
