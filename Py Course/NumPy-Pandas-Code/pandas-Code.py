#  (Great Learning - course)

import pandas as pd


""" Creation of series using dictionaries in Pandas """
sample_dict = {"x":1,"y":2,"z":3}
the_series = pd.Series(sample_dict)
# print(the_series)


""" Assign an name to an index in pandas: """
sample_series = pd.Series(list('123456789'))
sample_series.name = 'numbers'
sample_series.head()
# print(sample_series)


""" Printing unique elements in two series """
# that are present in one, not in the other
first_series = pd.Series([1,2,3,4,6])
second_series = pd.Series([5,6,7,8])
new_series = first_series[~first_series.isin(second_series)]
# print(new_series)