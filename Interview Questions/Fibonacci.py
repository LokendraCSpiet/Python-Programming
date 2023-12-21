"""
Write a program to find a fibonacci of a number.
"""

def fibonacci_1():
    first = 0
    second = 1
    print(first)
    while(second <= number):
        print(second)
        comp = first
        first = second
        second = comp + second

def fibonacci_2():
    first = 0
    second = 1
    nth = 0
    while(first <= number):
        print(first)
        nth = first + second
        first = second
        second = nth


number = int(input("Enter Number:"))
fibonacci_1()
# fibonacci_2()