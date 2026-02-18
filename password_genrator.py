import random
import string

print("this is used to genrate random password based on the user password length")
length=int(input("enter password length"))

charecters=string.ascii_letters+string.digits+string.punctuation

password=""

for i in range(length):
    password+=random.choice(charecters)

print("yor genrated password is")
print(password)