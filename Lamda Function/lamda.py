# Lambda Function
g = lambda x: x*x*x
print(g(3))


# Lambda Function (filter, map, reduce)

# Lambda function with filter takes two parameter
Li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(filter(lambda x:(x%2 != 0),Li))
print(final_list)

#  Lambda Function with map
Li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(map(lambda x: x*2, Li))
print(final_list)


# Lambda function with reduce
from functools import reduce
Li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x,y : x+y),Li)
print(sum)