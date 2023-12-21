"""

Write a program to print the following pattern.
A
B B
C C C
D D D D
E E E E E

"""

n = 5
ascNo = 65
for i in range (n):
    for j in range(i+1):
        print(chr(ascNo),end=" ")
    print("\r")
    ascNo += 1
