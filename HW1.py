# HW1.py
# Author: Tai Tran

# Question 1:
# Print Hello World like we did in class
print("Hello World")

# Question 2:
# Print the following:
# Your name
print("Tai Tran")

# Your age
print("19")

# Your favorite color
print("Blue")

# Your favorite animal
print("Wolf")

# Question 3:
# Create a variable called "myName" and set it equal to your name
myname = "Tai Tran"

# Create a variable called "myAge" and set it equal to your age
myAge = 19

# Create a variable called "myColor" and set it equal to your favorite color
myColor = "Blue"

# Create a variable called "myAnimal" and set it equal to your favorite animal
myAnimal = "Wolf"

# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>
print("Hello, my name is", myname)
print("I am", myAge, "years old")
print("My favorite color is", myColor)
print("My favorite animal is", myAnimal)

# Question 4:
# Calculate the following and print the result:
# 2 + 2
print(2 + 2)

# 3 * 4
print(3 * 4)

# 5 - 6
print(5 - 6)

# 8 / 2
print(8 / 2)

# Question 5:
# Create a variable called "num1" and set it equal to 2
num1 = 2

# Create a variable called "num2" and set it equal to 3
num2 = 3

# Create a variable called "num3" and set it equal to 4
num3 = 4

# Create a variable called "num4" and set it equal to 5
num4 = 5

# Calculate the following and print the result:
# num1 + num2
num1 + num2
print(num1 + num2)

# num3 * num4
num3 * num4
print(num3 * num4)

# num4 - num1
num4 - num1
print(num4 - num1)

# num2 / num1
num2 / num1
print(num2 / num1)

# Question 6: Write a program that asks the user for their name and then prints the following:

# Hello, <name>. Please enter three numbers. 
username = input("Enter your name: ")
print()
print("Hello,", username + ".", "Please enter three numbers.")
print()

# The program should then ask the user for three numbers (floats) and print the following:
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
print()

# 1. The sum of the three numbers is <sum>
sum = number1 + number2 + number3
print("The sum of the three numbers is", sum) 
print()

# 2. The product of the three numbers is <product>
product = number1 * number2 * number3
print("The product of the three numbers is", product)
print()

# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3
roundedSum = round(number1) + round(number2) + round(number3)
print("The sum of the three rounded numbers divided by 3 is", roundedSum / 3)
print()

# 4. The average of the three numbers is <average>
average = sum / 3
print("The average of the three numbers is", average)
print()

# Question 7: Ask the user for an input of a symbol (in the example its *)
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character.
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |

symbol = input("Please enter a symbol (for example, *): ")
print("You entered: ", symbol)
print()
print("     " +symbol, end="     |\n")
print("    " +symbol*3, end="    |\n'")
print("  " +symbol*5, end="   |\n")
print("  " +symbol*7, end="  |\n'")
print("  " +symbol*5, end="   |\n'")
print("   " +symbol*3, end="    |\n'")
print("    " +symbol*1, end="     |\n'")



