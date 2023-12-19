""" 
Write a Python program to find the largest element in a list.
"""

list1 = [5,4,8,73,8,77,44]

max = 0
for i in list1:
    if (i > max):
        max = i
print(f"the largest number is : {max}")