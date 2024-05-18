#  (Great Learning - course)

import numpy as np


eye_mat = np.eye(3)
print(eye_mat)

print_random = np.random.randint(0,100,10)
print(print_random)


# Print the 3r element of the 2nd row in a 3D array
numbers = np.array([[5,8,3],[3,1,2],[5,7,8]])
print(numbers[1][2])

# With a 5*5 array, let us insert numbers 1 to 25:
numbers2 = np.arange(1,26).reshape(5,5)
# numbers2 = np.arange(1,26)
print(numbers2)

# Replacing all of the even numbers with 10:
numEven_10 = np.array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
numEven_10[numEven_10%2==0] = 10
print(numEven_10)

# Converting 1D array into a 2D array
num1_2d = np.arange(10).reshape(2,-1)
print(num1_2d)


# Printing common elements from two NumPy Array:
x = np.array([10, 6, 30, 45])
y = np.array([36, 85, 10, 2, 7, 30])
common = np.intersect1d(x,y)
print(common)


# Print custom range values in an array
# Numbers from 3 to 6 are printing using a logical operation:
numRange = np.arange(10)
print(numRange)
numRange = numRange[(numRange >= 3) & (numRange <= 6)]
print(numRange)