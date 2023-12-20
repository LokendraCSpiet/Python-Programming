"""
Write a program to check if the given strings are anagram or not.
"""

def is_anagram(s1,s2):
    if(sorted(s1) == sorted(s2)):
        return True
    else:
        return False


s1 = input("Enter String 1 :")
s2 = input("Enter String 2 :")
if(is_anagram(s1,s2)):
    print(f"{s1} and {s2} is anagram")
else:
    print(f"{s1} and {s2} is not anagram")