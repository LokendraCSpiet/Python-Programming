"""

Write a program to print the following pattern.
*
* *
* * *
* * * *
* * * * *

"""


for i in range(1,6):
    str = ""
    for j in range(0,i):
        str += "* "
    print(str)


def myfunc(n):
    for i in range(1, n+1):
        for j in range(0, i):
            print("* ",end="")
        print("\r")

n = 5
myfunc(n)