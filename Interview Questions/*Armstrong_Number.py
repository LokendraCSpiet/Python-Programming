"""
Write a program to check if the given number is Armstrong or not
   (Armstrong - 0, 1 , 153, 370, 371, 407, 9474, 1634)
"""

def lengthNumber(num):
    count = 0
    while(num > 0):
       num = int(num / 10)
       count += 1
    return count

def is_armstrong(num):
    number = num
    power = lengthNumber(number)

    total = 0
    while(num > 0):
        rem = num % 10
        total += rem**power
        num = int(num / 10)
    
    if(total == number):
        return True
    else:
        return False
    
n = 5
while(n <= 5):
    num  = int(input("Entyer Number:"))
    if(is_armstrong(num)):
        print(f"{num} is a Armstrong Number")
    else:
        print(f"{num} is not a Armstrong Number")
    n += 1
