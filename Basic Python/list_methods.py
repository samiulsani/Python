
numbers=[10,20,30,40,50,60,70,80,90,100]
print(numbers)

# append() add the value to the end of the list

numbers.append(58)
print(numbers)

# insert() insert the value at the position

numbers.insert(1,90)
print(numbers)

# remove() delete the value from the list.

numbers.remove(90)
print(numbers)

if 90 in numbers:
    numbers.remove(90)
print(numbers)

# pop() remove last elements from the list
# we can also receive the value which is pop()

value=numbers.pop()
print(value,numbers)

# index() we can see the index of the value

index=numbers.index(20)
print(index)

# count() count the value from a list

count=numbers.count(20)
print(count)

# reverse() reverse the full list

numbers.reverse()
print(numbers)

# sort() sort the list

numbers.sort()
print(numbers)