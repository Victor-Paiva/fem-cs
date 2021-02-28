import numpy as np

def linear_search(array, key):
    for i, element in enumerate(array):
        if element == key:
            return i
    return None

array = np.random.randint(low=0, high=101, size=50)
print(array)
key = int(input('Insert a number between 0 and 100: '))
print(linear_search(array, key))