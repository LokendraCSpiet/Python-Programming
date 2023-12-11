""" 
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java 
"""
fileName = input("Sample filename:")
fileList = fileName.split(".")
ext = fileList[-1]
print(ext)