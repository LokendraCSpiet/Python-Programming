Item = [14,3,20,6,1,8,15,40]
evenItem = list(filter(lambda x:(x%2==0),Item))
oddItem = list(filter(lambda x:(x%2!=0),Item))
print(evenItem)
print(oddItem)
