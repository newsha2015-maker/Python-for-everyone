# Part 2: Functions and Modules

# Write a function called calculate_average that takes a list of numbers as input and returns the average.
# Create a module named my_math containing functions to calculate the square and cube of a number.
# Explain the difference between local and global variables in Python, providing examples.

import statistics
print("\n== Homework: Part 2: Functions and Modules ==")
print("\n== Calculate Avarage of list of Numbers ==")

user_input = input("Enter your numbers: ")             # Enter the list of numbers
numbers = [float(x) for x in user_input.split()]       # Split the string into a list of numbers 
                                                       # use float(x) instead of int(x)

print(numbers)
average = statistics.mean(numbers)
print(f"The average is: {average}")
