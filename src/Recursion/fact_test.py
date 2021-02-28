def closure():
    cache = [1]
    def compute(n):
        if n <= len(cache):
            return cache[n-1 if n-1 > 0 else 0]

        res = n * compute(n-1)
        cache.append(res)
        return res
    return compute

c = closure()
print(c(5))