
# return multiple value from a function at a time

def all_value(num1,num2):
    sum=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return sum,sub,mul,div # return value as a tuple
    #return [sum,sub,mul,div] # return value as a list

value=all_value(40,20)
print(value)
