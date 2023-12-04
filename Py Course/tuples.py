tuple1 = (11,2,3,5,8,10)

sorted(tuple1)
sorted(tuple1, reverse=True)

print(sorted(tuple1))
print(sorted(tuple1, reverse=True))


print("Tuple 2:")
tuple2 = ((4,1),(2,6),(1,2),(3,4))


def last(a):
    return a[-1]

print(sorted(tuple2))
print(sorted(tuple2, reverse=True))

print(sorted(tuple2, key=last))
print(sorted(tuple2, key=last, reverse=True))

print(sorted(tuple2, key=lambda last:last[-1]))
print(sorted(tuple2, key=lambda last:last[-1],reverse=True))


