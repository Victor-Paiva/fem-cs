def my_map(array, fn):
    return [fn(x) for x in array]

ls = list(range(11))
new_ls = my_map(ls, lambda x: x**3)

print('old list:\n\t', ls)
print('new list:\n\t', new_ls)