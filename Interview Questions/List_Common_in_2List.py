""" 
Write a Python program to find the common elements between two lists.
"""

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

# Test the function
list_a = [1,5,7,9,4]
list_b = [3,6,8,5,10,7]
print(find_common_elements(list_a, list_b))