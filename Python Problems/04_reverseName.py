"""
Write a Python program that accepts the user's first and last name 
and prints them in reverse order with a space between them.
"""

def reverseNAme(name):                                    # Method 3
    str = []
    string = ''
    for i in range(len(name)):
        str.insert(0,name[i])
    for j in range(len(name)):
        string = string + str[j]
    return string

def reverseName2(name):                                   # Method 2
    strList = []
    for i in name:
        strList.append(i)
    strList.reverse()
    s = ""
    revName = s.join(strList)
    return revName

def reverseName3(name):                                   # Method 3
    revName = ""
    for i in name:
        revName = i+revName
    return revName

fname = input("First Name: ")
lname = input("Last Name: ")
print("(1): "+lname+" "+fname)

rev_fname = reverseNAme(fname)
rev_lname = reverseNAme(lname)

print("(2): "+rev_lname + ' ' + rev_fname)