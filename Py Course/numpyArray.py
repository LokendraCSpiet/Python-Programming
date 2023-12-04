height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(type(np_weight))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
# bmi > 23
# print(bmi > 23)

# Print only those observations above 23
# bmi[bmi > 23]
# print(bmi[bmi > 23])

