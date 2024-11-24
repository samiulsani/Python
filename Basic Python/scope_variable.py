
# Local and global variable 

balance=500 # This is global variable

def value(item,numbers):
    # To access global variable use keyword 'global'
    global balance
    print(balance)

    # This is local scope variable
    balance=100
    print(balance)

    

value(10,20)