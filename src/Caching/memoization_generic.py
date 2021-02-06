def memoize(function):
    cache = {}
    def wrapper(*args):
        arg = tuple([*args])
        if arg not in cache.keys():
            # print('Calculating...')
            cache[arg] = function(*args)
        
        return cache[arg]
    return wrapper

@memoize
def times10(n):
    return n * 10

for n in [1, 2, 2, 2, 3, 4]:
    print(times10(n))