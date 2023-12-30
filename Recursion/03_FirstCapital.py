""" 
Given a String T, find the 1st occurrence of the capital (uppercase) alphabet. 
Print its index if present, else -1.

    For Example:
        Input : T = prepBytes
        Output : 4

        Input : T = helloWorld
        Output : 5
 """

def first_upper(T,n):
    if (n == len(T)):
        return -1
    char = T[n]
    if(ord(char) >= 65 and ord(char) <= 90):
        return n
    else:
        return first_upper(T,n+1)

for _ in range (int(input())):
    T = input("Enter your word:")
    print(first_upper(T,0))

