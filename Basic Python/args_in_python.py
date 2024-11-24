
# args function received two or more value as a parameter
# Basically args received more arguments when it's not define. But need to " * " before the numbers.



def all_value(num1,num2):
    print(num1,num2)

all_value(20,30)


#This is the args function

def all_value(num1,num2,*numbers):
    print(num1,num2,*numbers)

all_value(20,30,40,50,60,70,80,90)


# Another method to print

def all_value(num1,num2,*numbers):
    print(num1,num2,)
    for num in numbers:
        print(num)

all_value(20,30,40,50,60,70,80,90)

