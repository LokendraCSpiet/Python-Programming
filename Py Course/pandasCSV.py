# Import pandas and read the cars.csv data
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('Py Course/cars.csv')
print(cars)
print(cars.columns)    # Print the column names



# Import the country.csv data: country
country = pd.read_csv('Py Course/country.csv')
print(country.iloc[2])

country.index = ["BZL","RUS","IND","CH","SAF"]
print(country)

country1 = pd.read_csv('Py Course/country.csv', index_col = 0)
print(country1.iloc[2])





