""" 
Write a Python program to check if a string is a palindrome.
"""

# METHOD 1
str1 = input("Enter Value:")
str2 = ""
for i in str1:
    str2 = i + str2
print(str1 == str2)


# METHOD 2

def is_palindrome(string):
    reverse_word = string[::-1]
    return string==reverse_word

word = str1
if is_palindrome(word):
    print(f"{word} is Palindrome")
else:
    print(f"{word} is Not a Palindrome")