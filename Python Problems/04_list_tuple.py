""" 
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

list1 = []
tuple1 = ()
value = input("Enter comma-separated numbers:")
list1 = value.split(",")
tuple1 = tuple(list1)
print(list1)
print(tuple1)