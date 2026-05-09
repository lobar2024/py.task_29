def my_cache(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@my_cache
def qimmat_hisob(n):
    time.sleep(0.1)
    return n ** 2

print(qimmat_hisob(10))  # sekin
print(qimmat_hisob(10))  # tez (keshdan)
