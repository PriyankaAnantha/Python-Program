import numpy as np
array = np.zeros((5, 5), dtype=int)


array[0, :] = 1    # first row
array[-1, :] = 1   # last row
array[:, 0] = 1    # first column
array[:, -1] = 1   # last column

print(array)