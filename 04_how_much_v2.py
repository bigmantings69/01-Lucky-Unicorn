# Function go here...
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

# Main routine goes here
how_much = num_check("How much would you"
                     " like to play with? ", 0, 10)

print("you will be spending ${}".format(how_much))
# print the
