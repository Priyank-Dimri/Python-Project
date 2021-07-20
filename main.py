# Addition program for positive numbers using loop, conditions, functions and modules

# Import image as module from image.py
import image

# Simple add function which return value as per user input
def my_add(num1, num2):
    if (num1 or num2) < 1:
        return "Not Positive"
    else:
        return num1+num2


print(image.my_image)

want_to_continue = 1
print("Welcome to addition")

# Using loop, conditional and error handling to check for the user input and program continuation
while want_to_continue == 1:
    try:
        number1 = int(input("Please input number 1: "))
        number2 = int(input("Please input number 2: "))
        addition = my_add(number1, number2)
        print(f"Addition of 2 numbers through add function is {addition}")
        want_to_continue = int(input("Do you want to continue, please enter 1 for continue or 0 to exit:"))
        if want_to_continue == 0:
            break
    except ValueError:
        print("you have not entered integer value")



