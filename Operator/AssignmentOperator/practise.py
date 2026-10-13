# write a progam to check which number is greater in give three number.
def checkGreatesOfThree(a, b, c):
    if(a > b):
        if(b > c):
            return a
        elif(a>c):
            return a
        return c
    elif(b>c):
        return b
    return c
result1 = checkGreatesOfThree(input('Enter the  first number : '),input('Enter the second number : '),input('Enter the third number : '))
print('The Greatest of three number is: ',result1)

def checkGreaterOfThree(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    return c
result3 = checkGreaterOfThree(input('Enter the  first number : '),input('Enter the second number : '),input('Enter the third number : '))
print(result3)

def checkGreaterOfThree(a,b,c):
    return a if (a>b and a>c) else b if(b>c) else c
result3 = checkGreaterOfThree(input('Enter the  first number : '),input('Enter the second number : '),input('Enter the third number : '))
print(result3)


