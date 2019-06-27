import pandas as pd
import numpy as np

# generating a random Series
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))

# generating a dataframe with 3 rows and four columns
df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns=["A", "B", "c", "D"])

# applying a np ufunc will preserve the indices (rows and columns)
print(np.exp(ser))
print(df * np.pi / 4)

# handling missing data (NaN)
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')
print(population/area) # NY is NaN
