""" 
Write a Python program to check if a number is prime.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if(num % i == 0):
            if(num == i):
                return True
            else:
                return False
    return True

number = 17
if is_prime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is not a Prime Number")