# logical operators are used to combine conditional statements. There are three logical operators in Python: and, or, and not.
# For boolean true and false values, the logical operators work as follows:
# and: returns True if both statements are true, otherwise returns False.
# or: returns True if at least one statement is true, otherwise returns False.
# not: returns True if the statement is false, otherwise returns False.

#and operator
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
print(10>5 and 5<10) #True
print(10>5 and 5>10) #False
print('rajnish' and 'python')

#or operator
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False
print(10>5 or 5<10) #True
print(10>5 or 5>10) #True

#not operator
print(not True) #False
print(not False) #True
print(not (10>5)) #False
print(not (10<5)) #True

#For non boolean values, the logical operators work as follows:
#zero considerd as false
#non zero considerd as true
#empty string, list, tuple, set, dictionary considerd as false
#non empty string, list, tuple, set, dictionary considerd as true

#and operator
#if x evaluates to true, then the result of x and y is y.
#if x evaluates to false, then the result of x and y is x.
print(10 and 20) #20
print(0 and 20) #0
print('rajnish' and 'python') #python
print('' and 'python') #''
print([] and [1,2,3]) #[]
print({} and {'a': 1}) #{}

#or
#if x evaluates to true, then the result of x or y is x.
#if x evaluates to false, then the result of x or y is y.
print(10 or 20) #10
print(0 or 20) #20
print('rajnish' or 'python') #rajnish
print('' or 'python') #python
print([] or [1,2,3]) #[1, 2, 3]
print({} or {'a': 1}) #{'a': 1}
print(10 and 20 or 30) #20

#not
print(not 10) #False
print(not 0) #True
print(not 'rajnish') #False
print(not '') #True