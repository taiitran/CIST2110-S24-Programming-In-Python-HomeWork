# HW5.py
# Author: Tai Tran

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list
foods = ["chicken", "beef", "pork", "pizza", "burger"]

# Question 2: Using the list from question 1, print the first and last element of the list
print(foods[0], foods[-1])


# Question 3: Using the list from question 1, print the 3rd element of the list
print(foods[2])

# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing
print(foods[0:3])

# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing
print(foods[-2:])

# Question 6: Using the list from question 1, create a for each loop that prints each element of the list
for food in foods:
    print(food)

# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order
for food in foods[::-1]:
    print(food)

# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)
for index, food in enumerate(foods):
    print(index, food)

# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list[1][0])


# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list
# You can not use the reverse() function

def reverse_list(list):
    new_list = []
    for i in range(len(list) - 1, -1, -1):
        new_list.append(list[i])
    return new_list

print(reverse_list([1, 2, 3, 4, 5]))
