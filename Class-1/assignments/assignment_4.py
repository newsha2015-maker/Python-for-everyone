"""
Assignment 4: Loops and Lists

1.  Create a list of your five favorite fruits.
2.  Use a `for` loop to iterate through the list and print each fruit on a new line.
3.  Create a second list of numbers from 1 to 10.
4.  Use a `while` loop to print the square of each number in the list.
"""

print("\n== Assignment 4: Loops and Lists")

fruit = ["Grapes", "Orange", "Watermelon", "Lechi", "Berries", "Peach"]  # Create a list of fruits
# print(f"{fruit}") #Testing

for fruit in fruit:  # for loop
    print(fruit)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] # Create a list from 1 to 10 
#print(f"{numbers}") #Testing
for numbers in numbers:
    print(numbers)

while count[numbers] < 9:        # What is going here??? 
    count = 0
    squred_number = numbers ** 2   # while loop
    print(squred_number)
    count = count + 1