# Part 1: Python Basics

# Write a Python program that takes a user's name as input and prints a personalized greeting message.

print("\n== Homework: Part 1: Pythan Basics ==")
print("\n== Personalized Greetings ==")
name = input("What is your name? ")    # User input into a variable name

print(f"Hello {name} and welcome to Introduction to Pythan for evreyone. Enjoy learning {name}!")

# Create a program to calculate the area of a rectangle. Take the length and width as input from the user.

print("\n== Calculate the area of a rectangle ==")
width = int(input("what is the width? "))   # User input width for the rectangle
length = int(input("what is the length? "))  # User input lenght for the rectangle
area = int(width * length)
print(f"The area of the rectangel is: {area}")

# Write a Python program to check if a given number is even or odd.