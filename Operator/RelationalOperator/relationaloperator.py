#Whenever comparison is required, relational operators are used. Relational operators are used to compare two values. The result of a relational operation is either True or False. The following are the relational operators in Python:
# < (Less than)
# > (Greater than)
# <= (Less than or equal to)
# >= (Greater than or equal to)
# == (Equal)
# != (Not equal)
print(10<2)
print(10>2)
print(10<=2)
print(10>=2)
print(10==2)
print(10!=2)
print('rajnish'>'python')
# print('rajnish'>10) #give TypeError: '>' not supported between instances of 'str' and 'int'
print('rajnish'> str(10))
print(True>False)
print([3,2,3]>[9,2,3]) #checked the first element of both lists, if they are equal then check the second element and so on. If all elements are equal then the list with more elements is considered greater.
print('rajnish'>'1') #Here this is check with the ascii value of the characters. The ascii value of 'r' is 114 and the ascii value of '1' is 49. So, 'rajnish' is greater than '1'.

# a=97, b=98, c=99, d=100, e=101, f=102, g=103, h=104, i=105, j=106, k=107, l=108, m=109, n=110, o=111, p=112, q=113, r=114, s=115, t=116, u=117, v=118, w=119, x=120, y=121, z=122
# A=65, B=66, C=67, D=68, E=69, F=70, G=71, H=72, I=73, J=74, K=75, L=76, M=77, N=78, O=79, P=80, Q=81, R=82, S=83, T=84, U=85, V=86, W=87, X=88, Y=89, Z=90
# 1=49, 2=50, 3=51, 4=52, 5=53, 6=54, 7=55, 8=56, 9=57, 0=48
# we can find the ascii value of a character using ord() function. For example, ord('a') will return 97.

#chaining of the relational operators.
#=> If all the comparison is true in the chain, then the result is True. If any comparison is false, then the result is False.
print(10<20<30) #True
print(10<20>30) #False
print(10>20<30) #False
print('rajnish'>'python'<'java') #False

a=10
b=20
if(a<b):
    print('a is less than b')
else:
    print('a is not less than b')
    
if(a==b):
    print('a is equal to b')
else:
    print('a is not equal to b')
    
#Equality operator (==) is used to check whether two values are equal or not. If they are equal, then it returns True, otherwise it returns False, never throw type error. The equality operator can be used to compare values of different data types. For example, 10==10.0 will return True because the integer 10 is equal to the float 10.0. Similarly, '10'==10 will return False because the string '10' is not equal to the integer 10.

print(10==10.0) #True
print('10'==10) #False
print('10'==str(10)) #True
print('rajnish'==str('rajnish')) #True
print(True==1) #True
print(False==0) #True
print(True==False) #False

#What is the difference between == and is operator?
#The == operator is used to compare the values of two objects, while the is operator is used to compare the identities of two objects. The == operator checks whether the values of two objects are equal, while the is operator checks whether two objects are the same object in memory. For example, two different lists with the same values will be considered equal by the == operator, but they will not be considered the same object by the is operator.

l1=[1,2,3]
l2=[1,2,3]
print(id(l1)) #id of l1 give the reference of the object in memory
print(id(l2)) #id of l2 give the reference of the object in memory
print(l1==l2) #True, because the values of l1 and l2 are equal
print(l1 is l2) #False, because l1 and l2 are not the same object in memory
l3=l1
print(id(l3)) 
print(l1==l3) #True, because the values of l1 and l3 are equal
print(l1 is l3) #True, because l1 and l3 are the same