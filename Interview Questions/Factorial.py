""" 
Write a Python program to find the factorial of a number.
"""

def factorial(number):
    num = 1
    for i in range(number):
        num = num * (i+1)
    return num

def fact_Recursion(number):
    if(number == 0):
        return 1
    else:
        return number * fact_Recursion(number-1)

# my try
def factorial(num):
    if(num == 1):
        return 1
    else:
        num = num * factorial(num - 1)
    return num



number = int(input("Enter Number:"))
fact = factorial(number)
fact = fact_Recursion(number)
print(f"the Factorial of {number} is {fact}")
