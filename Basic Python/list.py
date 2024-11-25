
# list and array are same

"""we can access list or array using index= 0,1,2,3,4,5....
or we can access list from the back side index_back= -1,-2,-3,-4.....
"""
numbers=[10,20,30,40,50,60,70,80,90,100]

print(numbers[3],numbers[-2])

# we can divide the program and access it

# list=[ start : end ] start and end before end index

print(numbers[2:7])

# we can also use this by increment step list=[ start : end : step]

print(numbers[2:7:2])

# we can access using negative index

print(numbers[7:2:-2])

# we can also use blank value

print(numbers[3:])

print(numbers[ :5])

print(numbers[:])

# This method use to reverse the list

print(numbers[::-1])