import pandas as pd
import numpy as np


""" NumPy Array To Pandas DataFrame Conversion """
sample_series = pd.Series(np.random.randint(1,20,25))
data_frame = pd.DataFrame(sample_series.values.reshape(5,5))
print(data_frame)