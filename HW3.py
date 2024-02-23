# HW3.py
# Author: Tai Tran

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
number = int(input("Enter a number: "))

def number_squared(number):
    return number ** 2

print(number_squared(number))

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
string = input("Enter a string: ")
letter = input("Enter a letter: ")
number = int(input("Enter a number: "))

def replace(string, letter, number):
    return string[:number] + letter + string[number + 1:]
print(replace(string, letter, number))


# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
number = int(input("Enter a number: "))
lower_bound = int(input("Enter a lower bound: "))
upper_bound = int(input("Enter an upper bound: "))

def within_bounds(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound
print(within_bounds(number, lower_bound, upper_bound))

# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
def generate_greeting(name1, age1, favorite_color1):
    return f"Hello, my name is {name1}. I am {age1} years old. My favorite color is {favorite_color1}."

print(generate_greeting("Tai", 19, "blue"))



# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4

def user_input() -> str:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    favorite_color = input("Enter your favorite color: ")
    return generate_greeting(name, age, favorite_color)
    return output

print(user_input())
print(generate_greeting("Tai", 19, "blue"))



# Question 6:
# import the random module and use it to generate a random number between 1 and 100

import random

def random_number() -> int:
    return random.randint(1, 100)

print(random_number())


# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)

import math

def square_root() -> float:
    return math.sqrt(16)

print(square_root())



# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
from sys import version as ver
def python_version() -> str:
    return ver
print(ver)


# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function

from os import getcwd
def current_directory() -> str:
    return getcwd()
print(getcwd())






