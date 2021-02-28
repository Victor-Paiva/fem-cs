def join_elements(array, join_string):
    res = ''
    for element in array[:-1]:
        res += element + join_string
    return res + array[-1]

print(join_elements(['a', 'b', 'c', 'd'], ', '))