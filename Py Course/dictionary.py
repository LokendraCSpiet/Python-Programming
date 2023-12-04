phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
# print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
#----------------------------------Condition---------------------------------------------------------------------------

if "Jake" in phonebook: 
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")

#----------------------------------Removing a value---------------------------------------------------------------------------

del phonebook["John"] 
""" OR """
phonebook["John"] = 938477566
phonebook.pop("John")
# print(phonebook)


#------------------------------Iterating over dictionaries-------------------------------------------------------------------------------

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#-------------------------------------------------------------------------------------------------------------