import numpy as np


def numpy_base_functions():
    arange_of_values = np.arange(start=0, stop=10, step=2) # Creates integer
    print(arange_of_values)
    group_zeroes = np.zeros(shape=(10, 5)) # Creates Floats ( Matrix of floats )
    print(group_zeroes)
    group_ones = np.ones(shape=(4,2))
    print(group_ones)
