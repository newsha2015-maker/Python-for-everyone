"""
Python Variables and Data Types Demonstration

This module demonstrates fundamental Python concepts including:
- Variable assignment and dynamic typing
- Different data types (int, float, complex, str)
- Type conversion and checking
- String operations and formatting
- Complex number operations

Author: Avnit
Date: 2026
"""

# Example 1: Basic variable assignment and type checking
print("=== Example 1: Variable Assignment and Type Checking ===")
a = 10  # Integer variable
b = 2.6 # Float variable

print(f"Value of a is: {a}, Type: {type(a)}")
print(f"value of b is: {b}, Type: {type(b)}")

# Example 2: Float data type
print("\n == Example 2: Float Data Type ==")
b = 1.1 # Float variable
print(f"value of b is : {b}, Type: {type(b)}")

# Example 3: Complex numbers
print("\n=== Example 3: Complex Numbers ===")
c = complex(a, b) #creating complex number from int and float
print(f"complex number is {c}, Type: {type(c)}")

 # Example 4: Mathematical operations with complex numbers
print("\n=== Example 4: Complex Number Operations ===")
result = a / c # Division of int by complex number      
print(f"Result of {a} /{c} = {result}")

# Example 5: Accessing complex number components
print("\n=== Example 5: Complex Number Components ===")
print(f"The real part of complex number is : {c.real}", sep="/", end="\n")

# Example 6: String variables and concatenation
print("\n=== Example 6: String Operations ===")
a = "newsha" #string variable (reassigning 'a')
b = "my name is " + a #string concatenation
c = a + b #another string concatenation
print(f"string a : {a}")
print(f"string b : {b}")
print(f"string c : {c}")

# Example 7: Alternative complex number creation
print("\n=== Example 7: Alternative Complex Number Syntax ===")
d = 1 +2J #direct complex number creation
print(f"complex number d: {d}, Tyep: {type(d)}")
print(f"Real part: {d.real}")
print(f"Imaginary part: {d.imag}")

# Example 8: Type conversion exmples
print("\n=== Example 8: Type Conversion ===")
# Converting string to integer
str_num = "100"
int_num = int(str_num)
print(f"String '{str_num}' converted to Integar: {int_num}, Type: {type(int_num)}")
 

# Converting float to string
float_num = 3.14
str_float = str(float_num)
print(f"float {float_num} convert to string: '{str_float}', Type: {type(str_float)}")

# Example 9: Variable naming conventions
print("\n=== Example 9: Variable Naming Conventions ===")
user_nam = 

# Example 10: Multiple assignment

# Tuple unpacking