'''
Arithmetic Operators
=============================

There are several types of arithmetic operators in Python, which are used to perform mathematical operations on numeric values. The following are the commonly used arithmetic operators:

+ Addition (+): Adds two operands.
+ Subtraction (-): Subtracts the second operand from the first.
+ Multiplication (*): Multiplies two operands.
+ Division (/): Divides the first operand by the second.
+ Floor Division (//): Divides the first operand by the second and returns the largest integer less than or equal to the result.
+ Modulus (%): Returns the remainder of the division of the first operand by the second.
'''
print(10+2) # Addition
print(10-2) # Subtraction
print(10*2) # Multiplication
print(10/2) # Division
print(10//2) # Floor Division
print(10%2) # Modulus
print(10**2) # Exponentiation

#For Division, the result is always a float, even if the division is exact. For example, 10/2 will return 5.0, not 5.
#For Floor Division, the result is always an integer, even if the division is not exact. For example, 10//3 will return 3, not 3.3333, but if any one of the arguments is a float, the result will be a float. For example, 10.0//3 will return 3.0.

#(+) is also used for the concatenation of strings. For example, "Hello" + " " + "World" will return "Hello World".
#But when we concatenate a string both should be of string type, otherise it will throw an TypeError. For example, "Hello" + 5 will throw an error. To avoid this we can use str() to convert the integer to string. For example, "Hello" + str(5) will return "Hello5".
print("Hello" + " " + "World") # Concatenation of strings
print("Hello" + str(5)) # Concatenation of string and integer

#(*) is also used for the repetition of strings. For example, "Hello" * 3 will return "HelloHelloHello".
#But when we repeat a string, the second operand should be an integer, otherwise it will throw an TypeError. For example, "Hello" * 3.5 will throw an error. To avoid this we can use int() to convert the float to integer. For example, "Hello" * int(3.5) will return "HelloHelloHello".
#when we convert int('r') it will throw a ValueError because 'r' is not a valid integer.
print("Hello" * 3) # Repetition of string
print(int("5") * 3) # Repetition of converted string

print(10**2) # Exponentiation
print(2**2) # Exponentiation
print(16**-2) # Exponentiation