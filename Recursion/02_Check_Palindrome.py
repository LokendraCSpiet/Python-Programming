""" 
PROBLEM STATEMENT(SIMPLIFIED):
    Given a number N, check whether the number is palindrome or not using recursion. 
    The palindrome number remains the same when its digits are reversed.   

    For Example : 
        Input : N = "12321"
        Output : YES

        Input : N = "123"
        Output : NO 
        Explanation : 123 is not equal to 321
 """


def is_palin(n,rev):
    if(n == 0):
        return rev
    
    rev = rev * 10 + n % 10
    n = n // 10
    return is_palin(n,rev)

    
for _ in range(int(input())):
    n = int(input())
    rev = is_palin(n,0)
    if(rev == n):
        print("YES")
    else:
        print("NO")
        print(f"Explanation : {rev} is not equal to {n}")