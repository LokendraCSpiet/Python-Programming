# referance - https://www.prepbytes.com/blog/recursion-articles/
"""
Given two characters C1, C2 and an integer K, print all the possible
K length combinations of both the characters. Print the combinations lexicographically.
    NOTE:
        1. Characters can be repeated.
        2. Consecutive C2 characters are not allowed.
    For Example:
        INPUT  - x y 3
        OUTPUT - 
            xxx
            xxy
            xyx
            yxx
            yxy
"""


def solve(s, a, b, n):
    if(n > 0):
        if(s == ""):
            solve(s + a, a, b, n-1)
            solve(s + b, a, b, n-1)
        else:
            if(s[len(s)-1] == b):
                solve(s + a, a, b, n-1)
            else:
                solve(s + a, a, b, n-1)
                solve(s + b, a, b, n-1)
    elif(n == 0):
        print(s)


# MY METHOD -
def combinations(s,a,b,k):
    if(k > 0):
        if(s == ""):
            combinations(s+a,a,b,k-1)
            combinations(s+b,a,b,k-1)
        else:
            if(s[-1] == b):
                combinations(s+a,a,b,k-1)
            else:
                combinations(s+a,a,b,k-1)
                combinations(s+b,a,b,k-1)
    elif(k == 0):
        print(s)


for _ in range(int(input())):
    
    a, b, n = input().split()
    n = int(n)
    s = ""
    solve(s, a, b, n)
    # combinations(s,a,b,n)