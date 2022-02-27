import random
# from colorama import Fore, Back, Style

# class style:
#     BRIGHT = '\033[1m'

def play_game():
    with open("test-word.txt") as word:
        words_list = word.read()
        word = list(map(str, words_list.split()))
        global the_word
        the_word = random.choice(word)
        count = 8
        print("Welcome to Mystery Word: the word-guessing game running right on *your* command line! It's YOU vs. THE COMPUTER. You word is", len(the_word), "letters long. Guess one letter a time.")
    display = ["_"] * len(the_word)
    incorrect_guesses = []
    while count > 0:
        if "_" not in display:
            print("You beat the computer! Congrats!")
            quit()
        guess = input("Make a guess: ").casefold()
        i = 0
        if len(guess) != 1:
            print("Please only use 1 character.")
        elif guess in the_word:
            for letter in the_word:
                if letter == guess:
                    display[i] = letter
                    print("Good guess!")
                i += 1
            print(display)
        else:
            incorrect_guesses.append(guess)
            count = count - 1
            print(incorrect_guesses)
            print("Sorry, no dice. You have", count, "guesses left. Try again.")
    print("The computer wins! Lo siento. The correct answer was {}.".format(the_word))

if __name__ == "__main__":
    play_game()