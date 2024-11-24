
# For declaring function in python we need to write first " def "
# def means defination

def double_it(num):
    double=num*2
    print(double)

double_it(5)


def numbers(num1, num2):
    sum=num1+num2
    return sum

total=numbers(20,33)
print("Your total number is ",total)


def even(num):
    total=num/2
    return total

divisor=input("Enter your number : ")
total=even(int(divisor))
print(total)


def even(num):
    total=num//2
    return total

divisor=input("Enter your number : ")
print(even(int(divisor)))