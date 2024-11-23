# in , not, not in, is, is not
# >, <, >=, <=, ==, !==
# and , or

a=6;

# if a>5:
#     print("5 is greater then",a)
# else:
#     print(a,"is greater then 5")


if a>6:
    print("5 is greater then",a)
elif a<7:
    print("Majhamaji man")
else:
    print(a,"is greater then 5")

boss=False;

# if boss is True:
#     print("Boss is False")
# else:
#     print("Boss is true")

if boss is not True:
    print("Boss is False")
else:
    print("Boss is true")

# && instead of this in python we use 'and' for comparison
if a>=6 and boss==True:
    print("That is correct answer")
else:
    print("That is wrong answer")

# || instead of this we use 'or'

if a>=6 or boss==False:
    print("That is correct answer")
else:
    print("That is wrong answer")