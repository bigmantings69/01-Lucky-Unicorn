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




