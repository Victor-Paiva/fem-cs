def join_elements(array, join_string):
    def recurse(index, result):
        result += array[index]
        if index == len(array) - 1:
            return result
        return recurse(index + 1, result + join_string)

    return recurse(0, '')

print(join_elements(['a', 'b', 'c', 'd'], ','))