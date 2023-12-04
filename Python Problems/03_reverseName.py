fname = input("First Name: ")
lname = input("Last Name: ")
print("(1): "+lname+" "+fname)

# Fully Reversed :-
def reverseNAme(name):
    str = []
    string = ''
    for i in range(len(name)):
        str.insert(0,name[i])
    for j in range(len(name)):
        string = string + str[j]
    return string

rev_fname = reverseNAme(fname)
rev_lname = reverseNAme(lname)

print("(2): "+rev_lname + ' ' + rev_fname)