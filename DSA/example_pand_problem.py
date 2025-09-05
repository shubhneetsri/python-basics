"""
Using Pandas, get the student name and class with score greater than or equal to 60
[{"name": "a", "class": 1, "score": 90},
{"name": "b", "class": 1, "score": 85},
{"name": "c", "class": 1, "score": 50},
{"name": "d", "class": 1, "score": 90}, 
{"name": "a", "class": 2, "score": 50},
{"name": "b", "class": 2, "score": 30},
{"name": "c", "class": 2, "score": 70},
{"name": "d", "class": 2, "score": 60}]
"""

import pandas as pd

data = [
    {"name": "a", "class": 1, "score": 90},
    {"name": "b", "class": 1, "score": 85},
    {"name": "c", "class": 1, "score": 50},
    {"name": "d", "class": 1, "score": 90}, 
    {"name": "a", "class": 2, "score": 50},
    {"name": "b", "class": 2, "score": 30},
    {"name": "c", "class": 2, "score": 70},
    {"name": "d", "class": 2, "score": 60}
]

df = pd.DataFrame(data)

filtered_df = df[df['score'] >= 60]

result = filtered_df[['name', 'class']]
print(result)

mean_scores = df.groupby('class')['score'].mean() #.reset_index()
print(mean_scores)

data = df.groupby('class')['score'].transform('mean')
print(data)