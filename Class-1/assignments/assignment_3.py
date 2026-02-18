"""
Assignment 3: Conditional Logic

1.  Write a script that asks the user for a number.
2.  If the number is greater than 100, print "The number is large."
3.  If the number is between 50 and 100 (inclusive), print "The number is medium."
4.  If the number is less than 50, print "The number is small."
5.  Include a check for the number being exactly 50 or 100.
"""
print("\n == Assignment 3: Conditional Logic ==")

number = int(input(f"Enter a number:"))   # Ask the user for a number
if number > 100: 
    print(f"The number is large.")
elif number >= 50 and  number <= 100:     # Check if number is between 50 and 100
    print(f"The number is medium.")
elif number < 50:
    print(f"Number is small.")            # Check if number is small 
else:
     print(f"The number is in fact bewteen 50 and 100")
