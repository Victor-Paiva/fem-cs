import random

def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True

array = list(range(20))
random.shuffle(array)
print('Original:\n', array)
bubble_sort(array)
print('Sorted:\n', array)
