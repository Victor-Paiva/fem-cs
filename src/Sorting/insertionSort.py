import random

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))

array = list(range(20))
random.shuffle(array)
print('Original:\n', array)
insertion_sort(array)
print('Sorted:\n', array)