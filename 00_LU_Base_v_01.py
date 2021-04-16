import random
<<<<<<< HEAD


# checks valid number has been entered
def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the questions
            response = int(input(question))
            # if the amount is too low ? too high give
            if low < response <= high:
                return response

                # output an error
            else:
                print(error)

        except ValueError:
                print(error)

# decorates statements to make them stand out


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""
=======
# Function go here..
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7


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


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("The rules of this game is simple. Enter the amount you'd like to play with.")
    print("When you begin playing, you'll receive a token.")
    print("There are four tokens:")
    print()
    print("*Unicorn which is worth $4")
    print()
    print("*Zebra and Horse, which are both worth -50 cents.")
    print()
    print("*Donkey, which is -$1.")
    print()
    print("Play until you are satisfied, or until you run out of money. Have fun!")
    print()

    return""


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

<<<<<<< HEAD
=======

def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the questions
            response = int(input(question))
            # if the amount is too low ? too high give
            if low < response <= high:
                return response

                # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here...
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7

# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have you played the ""game before? ")

if played_before == "no":
    instructions()

<<<<<<< HEAD
if played_before == "yes":
    start()
=======
print()

>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7

# Ask user how much they want to play with...
how_much = num_check("How much would you"
                     " like to play with? ", 0, 10)

print("you will be spending ${}".format(how_much))

# set balance for testing purposes
balance = how_much

rounds_played = 0

play_again = input("press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random #is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
<<<<<<< HEAD
        prize_decoration = "!"
=======
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7
        balance += 4

    # if the random# is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
<<<<<<< HEAD
        prize_decoration = "D"
        balance -= 1

=======
        balance -= 1
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7
    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is eve, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
<<<<<<< HEAD
            prize_decoration = "H"
=======
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7

            # otherwise set it to a zebra
        else:
            chosen = "zebra"
<<<<<<< HEAD
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is " \
                  "${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

=======
        balance -= 0.5

>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

<<<<<<< HEAD
    print()
    print("results")
    prize_decoration = "="
    print()

    print("You got a {}.  Balance: ${:.2f}".format(chosen, balance))

print()
print("Final balance: ${:.2f}".format(balance))
=======
    print("You got a {}.  Balance: ${:.2f}".format(chosen, balance))

print()
print("Final balance", balance)
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7
