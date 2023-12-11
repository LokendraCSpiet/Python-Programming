""" 
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

n = input("Enter n:")
result = int(n)+int(n+n)+int(n+n+n)
print(result)


a = int(input("Input an Integer:"))
result = a+int(str(a)+str(a))+int(str(a)+str(a)+str(a))
print(result)
