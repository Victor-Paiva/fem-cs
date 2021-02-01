def uniqSort(array):
    new_array = []
    cache = {}
    for element in array:
        if element not in cache.keys():
            cache[element] = True
            new_array.append(element)

    new_array.sort()
    return new_array

array = [3, 3, 4, 1, 1, 1, 2]
print(uniqSort(array))