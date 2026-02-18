import random

print("welcome to the random guessing game")

secret_number = random.randint(1,100)
attempts = 0

while True:
    guessing_no = int(input("enter the guessing number"))
    attempts+=1
    if guessing_no==secret_number:
        print("correct")
        break
    elif guessing_no>secret_number:
        print("too high")
    elif guessing_no<secret_number:
        print("too low")
    if attempts==5:
        break   
