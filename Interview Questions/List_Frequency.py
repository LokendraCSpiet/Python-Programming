""" 
Write a Python program to count the frequency of each element in a list.
"""

def count_frequency(list):
    frequency = {}
    for i in list:
        if i in frequency:
            frequency[i] = frequency[i]+1
        else:
            frequency[i] = 1
    return frequency

list1 = [1,2,1,5,4,1,3,4]
print(count_frequency(list1))