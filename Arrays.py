import time
import numpy as np

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
print(1.0 / values)  # takes less than 11 milliseconds, using ufuncs
end = time.time()
print(end-start)

# ufuncs in numpy are also useful for mean, max-min etc.
big_array.mean()
big_array.max()
