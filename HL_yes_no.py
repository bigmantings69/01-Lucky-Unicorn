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

