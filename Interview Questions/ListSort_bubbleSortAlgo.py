"""
Write a Python program to sort a list of elements using the bubble sort algorithm.
"""

# METHOD 1 - 
def sort_list(list):
    for i in list:
        n = 1
        for j in list:
            if n == len(list):
                continue
            if j > list[n]:
                list[n-1] = list[n]
                list[n] = j
            n += 1
    return list


# METHOD 2 - 
def bubble_sort(elements):
    n = len(elements)
    for i in range(n-1):
        for j in range(n-i-1):
            if elements[j] > elements[j+1]:
                elem = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = elem
    return elements



list1 = [8, 7, 3, 1, 2]
print(sort_list(list1))
print(bubble_sort(list1))