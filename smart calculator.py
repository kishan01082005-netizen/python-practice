def add(*a):
    total = 0 
    for num in a:
        total+=num
    return total
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

op = input("enter the operation to be performed: ")
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))

if op=="add":
    print(add(a,b))
elif op=="sub":
    print(sub(a,b))
elif op=="mul":
    print(mul(a,b))
else:
    print(div(a,b))
     