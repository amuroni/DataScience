import time
import numpy as np
import pandas as pd

start = time.time()
np.random.seed(0)


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


values = np.random.randint(1, 100, size=100)
big_array = np.random.randint(1, 100, size=1000000)
# compute_reciprocals(big_array)  # this is slow, takes approx 2s to run
print(1.0 / values)  # takes milliseconds, using ufuncs
end = time.time()
print(end-start)

# ufuncs in numpy are also useful for mean, max-min etc.
print(big_array.mean())
print(big_array.max())

b = np.random.rand(1, 10)  # generates a random array, 1 row and 10 items
print(b)

data = pd.Series([1, 2, 3, 4, 4.5, 5])  # a panda series is a one dimensional array
data.index = ["a", "b", "C", "d", "e", "f"] # a custom index can be assigned
print(data["d"])  # is like accessing values from a dictionary

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

population = pd.Series(population_dict)
print(population["California"])  # access Cali population in the dict

random_series = pd.Series(np.random.randint(1, 10, size=10))

# creating a Pandas dataframe

area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995}

area = pd.Series(area_dict)
states = pd.DataFrame({"population": population, "area": area})  # combines teo series in a df
print(states.index)  # index attributes
print(states.columns)  # columns attributes
print(states["area"])  # returns the area column
print(states.area)  # same as before, if column names are strings
print(states["area"] is states.area)  # hint: True

# creating a random pd df
random_df = pd.DataFrame(np.random.rand(3, 2), columns=["foo", "bar"], index=[1, 2, 3])
print(random_df["foo"][1])  # returns the value stored with index 1 in column foo
print(random_df.loc[2])  # easier to localize specific values based on index

# modifying the dataframe
states["density"] = states.population/states.area  # this adds a column and put values into it
print(states.values)  # puts ALL the values in a one-dimensional array
print(states.T)  # transpose columns/rows
