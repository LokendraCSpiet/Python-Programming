"""

Write a program to print the following pattern.
    *
   * *
  * * *
 * * * *
* * * * *

"""

n = 5
for i in range(1,n+1):
    for sp in range(0,n-i):
        print(" ",end="")
    for star in range(i):
        print("*",end="")
    print("\r")