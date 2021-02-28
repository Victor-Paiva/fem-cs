def my_filter(ls, fn):
    return [x for x in ls if fn(x)]

ls = list(range(31))
new_ls = my_filter(ls, lambda x: not x%2)

print('old list:\n\t', ls)
print('new list:\n\t', new_ls)