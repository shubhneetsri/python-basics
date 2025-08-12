"""
In a dataset of employee records, 
some entries in the 'Salary' column are missing. 
You are tasked with imputing these missing values based on department averages. 
Explain how you would accomplish this using Pandas.
"""

import pandas as pd
# import numpy as np

# read the file

# One Dimentional Array :: Series
# s = pd.Series([10,20,30], index = ['a', 'b', 'c'])
# print("\nOne Dimentional Array :: Series")
# print(s)

# Two DImentional Data :: DataFrame
# Sample dataset
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, None, None, 65000]
}

df = pd.DataFrame(data)

# Step 1–2: Compute department average salaries and align them to each row
df['dept_avrg'] = df.groupby('Department')['Salary'].transform('mean')
df['new_salary'] = df['Salary'].fillna(df['dept_avrg'])
print(df)
# Step 3: Fill missing salaries with department averages
# df['Salary'] = df['Salary'].fillna(dept_avg)

# print(df)

# df = pd.DataFrame(data)
# print("\nTwo DImentional Data :: DataFrame")
# print(data)
# print("\nFirst 5 rows :: head():")
# print(df.head())
# print("\nLast 3 rows :: tail():")
# print(df.tail())
# print("\nRows and Colm :: shape:")
# print(df.shape)
# print("\nSummary of DatFrame :: info():")
# print(df.info())
# print("\nStatistical Summary :: describe():")
# print(df.describe())

# print("\nSelect Data: Series")
# print(df['Name'])
# print(df[['Name']])

# print(df.iloc[0])

