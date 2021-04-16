# Function go here...


# Main routine goes here

error = "Please enter an whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask the questions
        response = int(input("How much would you "
                             "like to play with? "))
        # if the amount is too low ? too high give
        if 0 < response <= 10:
            print("You have asked to play "
<<<<<<< HEAD
                   "with ${}".format(response))
=======
                  "with ${}".format(response))
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7

            # output an error
        else:
            print(error)

    except ValueError:
<<<<<<< HEAD
            print(error)

=======
        print(error)
>>>>>>> ff1f159f50e30777e9ea857ef772ede39ac76bb7
