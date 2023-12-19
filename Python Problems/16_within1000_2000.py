""" 
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

# 1000 => True
# 900  => True
# 800  => False
# 2200 => False

number = int(input("Enter Number:"))


if(abs(1000 - number) <= 100 or abs(2000 - number) <= 100):
    print(True)
else:
    print(False)
