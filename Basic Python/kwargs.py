
# kwargs like args but kwargs received parameter without maintain sequence


# Take parameter in serially.........
# def full_name(first,last):
#     name=f'{first} {last}'
#     return name

# name=full_name(
#     'samiul','islam'
# )

# print(name)


# Take parameter without serial.............

# def full_name(first,last):
#     name=f'{first} {last}'
#     return name

# name=full_name(last='samiul',first='islam')

# print(name)

#----------------------------

# def function_name(**kwargs). it's mean key

# def full_name(first,last,**addition):
#     name=f'{first} {last}'
#     print(addition)
#     return name

# name=full_name(first='samiul',last='islam',title='doctors',addition='jamalpur')
# print(name)



# We can also write like this. we can also see key and value differently.

def full_name(first,last,**addition):
    name=f'{first} {last}'
    for key,value in addition.items():
        print(key,value) # see the key and value. like "title" is key
    return name

name=full_name(first='samiul',last='islam',title='doctors',addition='jamalpur')
print(name)

