'''
Data type represent the type of data represented by a variable.

Fundamental data types in Python:
    int
    float
    complex
    string
    bool

collection data types in python:
    list
    tuple
    dict
    set
    frozenset
    bytes
    bytearray
    range
    none
'''

# In python everything is treated as object

# In python most commonly user function is print(), type(), id()

# INT => To represent the integral value

x = 10
print(x)

'''
we can write integral value ini different form
    Decimal (base 10)       => 0-9
    Boolean (base 2)        => 0-1
    octadecimal (base 8)    => 0-7
    hexadecimal (base 16)   => 0-9 , A-F
'''
x = 10
print(x)

x = 0b11
print(x)

x = 0b10
print(x)

x = 0B00
print(x)

x = 0B1111
print(x)


x = 0o17
print(x)

# x = 0o19 => error because octal range is 0-7
# print(x)

x = 0x12c
print(x)

# Base conversion function

# bin()
# oct()
# hex()

x=10
print(bin(x))

x=0b01
print(oct(x))

x = 0b11
print(hex(x))
