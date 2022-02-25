import random

from pyparsing import Word


# def random_word():
#     for r_words in words:



def play_game():
    with open("test-word.txt") as word:
        words_list = word.read()
        word = list(map(str, words_list.upper().split()))
        global the_word
        the_word = random.choice(word).upper()
        print("Welcome to Mystery Word: the word-guessing game running right on *your* command line! It's YOU vs. THE COMPUTER. You word is", len(the_word), "letters long. Guess one letter a time.")
        guesses = input("Make your first guess: ")
        print([letter if letter in guesses else "_" for letter in the_word])
        # if the guess contains a correct letter, give a great! and prompt for further guesses
        # if the guess doesn't contain a correct letter, give a "no dice!" and prompt for further guesses


#from Jupyter

# word = "MAGNITUDINAL"
# current_guesses = []

# def display_letter(letter, guesses):
#     """
#     Conditionally display a letter. If the letter
#     is already in the list `guesses`, then return it.
#     Otherwise, return "_".
#     """
#     if letter in guesses:
#         return letter
#     else:
#         return "_"
# # we want to call the display_letter method
# [display_letter(letter, current_guesses) for letter in word]

# word = "MAGNITUDE"
# guesses = []

# def print_word(word, guesses):
#     output_letters = [display_letter(letter, guesses)
#                         for letter in word]
#     print (" ".join(output_letters))

# # print_word(word, guesses)

# #would this be for evil method?
# word = "MAGNITUDE"
# guesses = ["G", "E", "T"]
# word = "NECESSITY"
# guesses = ["E", "T", "S", "N"]

# [letter
#     for letter in word
#     if letter in guesses]

# choose a random value
# keep track of state
# "Welcome to Mystery Word: the word-guessing game running right on *your* command line! It's YOU vs. THE COMPUTER. Let's go! Choose a word."
# I would love for red asterisks when the answer is wrong saying, "Bad luck! That's not the word."
# I would love yellow astersisks when the answer is close that gives clues
# I would love rainbow asterisks for when the answer is correct.
# Look into ascii text art when the code is written and the game is solid.
# only allow 8 guesses
# put a count on the guesses
# create an empty list of guesses

if __name__ == "__main__":
    play_game()
