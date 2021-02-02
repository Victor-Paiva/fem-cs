def naive_factorial(n):
    return 1 if n < 2 else n * naive_factorial(n-1)

def factorial(n, cache=[1]):
    if n < 2:
        return 1

    if len(cache) >= n:
        return cache[n]
    
    ans = n * factorial(n-1)
    cache.append(ans)
    # print(cache)
    
    return ans

f = 20
print(naive_factorial(f), factorial(f))