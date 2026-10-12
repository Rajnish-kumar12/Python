#Bitwise operator are only used for the boolena value and integer value. There are six bitwise operators in Python: &, |, ^, ~, <<, and >>.
#&: AND operator, returns 1 if both bits are 1, otherwise returns 0.
print(10 & 20) #0
print(10 & 30) #10

#|: OR operator, returns 1 if at least one bit is 1, otherwise returns 0.
print(10 | 20) #30
print(10 | 30) #30

#^: XOR operator, returns 1 if the bits are different, otherwise returns 0.
print(10 ^ 20) #30
print(10 ^ 30) #20

#~: NOT operator, returns the complement of the number.
print(~10) #-11
print(~30) #-31

print(~-10) #9

'''
The most significant bit (MSB) is the leftmost bit in a binary number. In Python, the MSB is used to represent the sign of the number. If the MSB is 0, the number is positive, and if the MSB is 1, the number is negative. The ~ operator flips all the bits of a number, including the MSB, which changes the sign of the number.
Positive number will directly store in memory, but negative number will store in memory as 2's complement. The 2's complement of a number is obtained by inverting all the bits and adding 1 to the least significant bit (LSB). For example, the 2's complement of 10 is -10, which is represented in binary as 11111111111111111111111111110110.
'''

#<<: Left shift operator, shifts the bits to the left by the specified number of positions.
print(10 << 2) #40

#>>: Right shift operator, shifts the bits to the right by the specified number of positions.
print(10 >> 2) #2