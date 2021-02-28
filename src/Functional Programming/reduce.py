def my_reduce(ls, fn, seed=None):
    res = seed if seed else ls[0]
    start = 0 if seed else 1
    for element in ls[start:]:
        res = fn(res, element)

    return res

ls = [x**2 for x in range(5, 0, -1)]
reduced = my_reduce(ls, lambda x, y: x*y)

print('before:\n\t', ls)
print('after:\n\t', reduced)