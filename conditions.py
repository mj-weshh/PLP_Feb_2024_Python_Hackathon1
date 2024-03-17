# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f

# Create a Python program that:
# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."


def voting_eligibility(age):
    if age >= 18:
        print('You are eligible to vote.')
    else:
        print('You are not eligible to vote.')


# handling a potential error if the users age input is invalid, i.e cannot be parsed into an int
try:
    # storing the users input in a variable named age
    age = int(input('Enter your age: '))

except ValueError:
    print('Error! Try again using an integer as your age input.')


# calling the voting_eligibility function and parsing age as the argument
voting_eligibility(age)