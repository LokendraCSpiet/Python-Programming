"""
Write a program to find GCD (Greatest Common Divisor) of two numbers.
Ex. = GCD of 20 and 15 is 5
"""

# FIRST METHOD (my method)
def divisible_List(number):
    num = number + 1
    list1 = []
    for i in range(1,num):
        if(number%i == 0):
            list1.append(i)
    return list1

def greatest_common_divisor(number1,number2):
    list1 = divisible_List(number1)
    list2 = divisible_List(number2)

    list1.reverse()
    list2.reverse()
    
    if(len(list1) < len(list2)):
        minList = list1
        largeList = list2
    else:
        minList = list2
        largeList = list1

    for i in minList:
        if i in largeList:
            return i


number1 = int(input("Enter Number 1 :"))
number2 = int(input("Enter Number 2 :"))

GCD = greatest_common_divisor(number1,number2)
print(f"GCD of {number1} and {number2} is : {GCD}")





# SECOND METHOD
def gcd(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a

    if (a == b):
        return a

    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

a = 98
b = 56
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')