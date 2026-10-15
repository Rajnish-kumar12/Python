class CheckGreatest:
    number_1 = 10
    number_2 = 20
    number_3 = 30
    
    def checkGreatest(self,number_1,number_2,number_3):
        if(number_1>number_2 and number_1>number_3):
            return number_1
        elif(number_2>number_3):
            return number_2
        else:
            return number_3
number_1 = 10
number_2 = 20
number_3 = 30
def sum(number_1,number_2,number_3):
    print(number_1+number_2+number_3)
    
def prod(number_1,number_2,number_3):
    print(number_1*number_2*number_3)