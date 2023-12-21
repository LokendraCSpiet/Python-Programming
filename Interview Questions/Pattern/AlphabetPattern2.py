"""

Write a program to print the following pattern.
A
B C
D E F
G H I J
K L M N O

"""

n = 5
ascNo = 65
for i in range (n):
    for j in range(i+1):
        print(chr(ascNo),end=" ")
        ascNo += 1
    print("\r")
