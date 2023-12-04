import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&*"
length = int(input("Enter pass Length:"))
password = ''

for i in range(length):
    password += random.choice(char)

print(password)
