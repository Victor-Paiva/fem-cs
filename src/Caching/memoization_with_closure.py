def factorial():
    cache = [1]
    def compute(n):
        if n < 2:
            return 1

        if len(cache) >= n:
            return cache[n]
            
        ans = n * compute(n-1)
        cache.append(ans)
        # print(cache)

        return ans

    return compute

fact = factorial()
print(fact(8))