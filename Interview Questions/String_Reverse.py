""" 
Write a Python program to reverse a string.
"""

string = "Hello"
print(string[::-1])

str1 = ""
for i in string:
    str1 = i + str1
print(str1)