"""
Write a program to check if the given number is palindrome or not.
"""

def is_pelindrome(num):
    number = num
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = rev*10 + rem
        num = int(num / 10)

    if(rev == number):
        return True
    else:
        return False


num = int(input("Enter A number:"))
if(is_pelindrome(num) == True):
    print(f"{num} is a Pelindrome")
else:
    print(f"{num} is not a Pelindrome")