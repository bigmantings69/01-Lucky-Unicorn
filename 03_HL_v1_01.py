import random


# instruction if user did not play the game before


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("For each game you will be asked to...")
    print("- Enter a 'low' and 'high' number. "
          "The computer will randomly generate a 'secret' number between your two chosen numbers."
          " It will use these numbers for for all the rounds in a given game.")
    print("- The computer will calculate how many guesses you are allowed")
    print("- enter the number of rounds you want to play")
    print("- guess the secret number")
    print()
    print("Good Luck!")


# decorating program to decorate the game

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# yes or no answer for the program


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please enter yes or no")


def statement_generator(outcome, prize_decoration):

    sides = prize_decoration * 3

    outcome = "{} {} {}".format(sides, outcome, sides)
    top_bottom = prize_decoration * len(outcome)

    print(top_bottom)
    print(outcome)
    print(top_bottom)

    return ""


def start():
    print()
    print("lets get started")
    print()
    prize_decoration = "-"
    return""


# introduction for the game
# ask if they have played this game before
# if no show instructions
# if yes continue

statement_generator("Welcome to Higher or lower", "*")
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

if played_before == "yes":
    start()


rounds_played = 0

play_again = input("press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))


# check a lowest is an integer (any integer)
# check that highest is more than lowest (lower bound only)
# check that rounds is more than 1 (upper bound only)
# lower and upper bound


# Number checking function goes here

def int_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # check input is not too high or
            # too low if a both upper and lower bounds
            # are specified
            if situation == "both":
                if response < low or response > high:
                    print("please enter a number between "
                          "{} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more "
                          "than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is a integer
        except ValueError:
            print("Please enter an integer")
            continue


# Main routine

lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)

# increase # of rounds played
rounds_played += 1

# print round number
print()
print("*** Round #{} ***".format(rounds_played))

# HL component 11 - Maximum Guesses Calculator

import math

for item in range(0,4):     # loop component for easy testing.....

    low = int(input("Low: "))  # use int check in due course
    high = int(input("High: "))  # use int check in due course

    range = high - low + 1
    max_raw = math.log2(range)  # finds maximum # of guesses using
    max_upped = math.ceil(max_raw)  # rounds up (ceil ---> ceiling)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()

# HL component 5 - prevents duplicate guesses

SECRET = 7
GUESSES_ALLOWED = 5

# list for guesses
already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))  # replace this with function

    # check that guess is not a duplicate

    if guess in already_guessed:
        print("You already guessed that number! Please try again"
              "you *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

        elif guess > SECRET:
            print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
    else:
        if guess < SECRET:
            print("Too Low!")
        elif guess > SECRET:
            print("Too High!")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED -1:
        print("Amazing! You got it")
    elif guess == SECRET:
        print("Well done, you got it")

