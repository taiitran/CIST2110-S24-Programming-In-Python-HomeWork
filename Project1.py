# Project1.py
# Author: Tai Tran


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.


# Write a function that displays a welcome message to the user and explains the rules of the game


# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:
# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.


# Function Utilization:

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, the correct answer, and return whether the user was correct.
# an example would be def ask_question(question:str, option_1:str, option_2:str, option_3,:str option_4:str, correct_answer:str)->bool:

# the return value should be a boolean (True or False) for whether the user was correct

# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).


print("Welcome to the Tai's Quiz Game!")
print("You will be asked a series of questions and you will need to answer them CORRECTLY.")
print("Each question will be worth 1 point.")
print(" ")

def ask_question(question:str, option_1:str, option_2:str, option_3:str, option_4:str, correct_answer:str)->bool:
    print(question)
    print(f"a) {option_1}")
    print(f"b) {option_2}")
    print(f"c) {option_3}")
    print(f"d) {option_4}")
    user_answer = input("Enter your answer: ").lower()

    while user_answer not in ["a", "b", "c", "d"]:
        print("Invalid input! Please enter a, b, c, or d.")
        user_answer = input("Enter your answer: ").lower()

    if user_answer == correct_answer:
        print("Correct! You got 1 point!")
        return True
    else:
        print("Incorrect! The correct answer is " + correct_answer + ".")
        return False
    
def final_score(score:int):
    print(f"Your final score is: " + str(score) + " points.")
    print("Thank you for playing! Goodbye!")

def quiz_game():
    questions = [
        ("1) What is Tai's favorite color?", "Red", "Blue", "Black", "White", "b"),
        ("2) What is Tai's dog's name?", "Taro", "Mocha", "Mochi", "Boba", "d"),
        ("3) What is Tai's favorite food?", "Pizza", "Burger", "Ramen", "Fried Chicken", "d"),
        ("4) What is Tai's favorite workout?", "Bench Press", "Squat", "Deadlift", "Pull ups", "a"),
        ("5) What is Tai's favorite ice cream flavor?", "Vanilla", "Chocolate", "Matcha", "Strawberry", "c")
    ]

    score = 0
    for question, option_1, option_2, option_3, option_4, correct_answer in questions:
        if ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
            score += 1
    final_score(score)


quiz_game()



















