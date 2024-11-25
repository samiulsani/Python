

numbers=[1,20,3,40,5,60,70,80,90]
odds=[] # we can create empty list to push or append value from an operation

for num in numbers:
    if num % 2 != 0:
        odds.append(num)

print(odds)

# we can do it in short method

number=[5,20,35,30,69,10,40,37]
odd_number=[num for num in number if num % 2 == 1]
print(odd_number)