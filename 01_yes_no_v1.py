# Ask the user if they have played before
show_instructions = input("Have you played this game " "before? ")

# If they say yes, output 'program continues'
if show_instructions.lower() == "yes":
    print("program continues")

elif show_instructions.lower() == "no":
    print("display instructions")

elif show_instructions.lower() == "y":
    print("program continues")

elif show_instructions.lower() == "n":
    print("display instructions")

# If they say no, output 'display instructions'
else:
    print("please answer yes or no")

# If the answer is invalid, print an error.
