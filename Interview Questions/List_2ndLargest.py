"""
Write a Python program to find the second largest number in a list.
"""

def second_largest(list1):

    if(list1[0] > list1[1]):
        max1 = list1[0]
        max2 = list1[1]
    else:
        max1 = list1[1]
        max2 = list1[0]

    n = len(list1)
    for i in range(2,n):
        if(list1[i] > max1):
            max2 = max1
            max1 = list1[i]
        elif(list1[i] > max2 and list1[i] != max1):
            max2 = list1[i]
    return max2

list1 = [25,121,5,7,66,121,-55,100]
print(second_largest(list1))
        

