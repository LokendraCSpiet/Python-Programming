list1 = [1,8,21,7,2,21,15]

list = ['larry', 'curly', 'moe']
if 'curly' in list:     # check in list
    print('yay') 

# Assignment with an = on lists does not make a copy. 
# Instead, assignment makes the two variables point to the one list in memory.
colors = ['red', 'blue', 'green']
b = colors              ## Does not copy the list
b.append("newColor")
print(b)
print(colors)



count = list1.count(21)   # count value in list
index = list1.index(7)    # gives index of value

list1.sort()            # sort the list
list1.reverse()         # reverse the list
list1.append(45)        # append in the end of list
list1.insert(2,544)     # insert 544 at 2 index  
popVal = list1.pop(2)            # remove value at 2 index and return value at 2
list1.remove(21)        # remove 21 only ones
list1[2] = 568

list1.extend(['yyy', 'zzz'])   ## add list of elems at end
print(list1)
print(popVal)


list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']


list2 = []
list2[0] = "55"         # not Assign to list
print(list2)

