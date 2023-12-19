"""
Write a Python program to remove duplicates from a list.
"""

def remove_duplicate(list1):
    newList = []
    for i in list1:
        if i not in newList:
            newList.append(i)
    return newList

list1 = [1,5,6,3,5,4,2,4,6,1,2,45,3]
print(remove_duplicate(list1))