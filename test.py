import pandas as pd
import numpy as np

df = pd.DataFrame([
    [1,2,3,4,5,6],
    ['admin','','internal','finance','',''],
    [200,300,1,34,4,900]
])

df.replace('',np.nan)
print(df.fillna('missing'))