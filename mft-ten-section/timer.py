import time


def timeit(fn):
    def inner(*args, **kwargs):
        t1 = time.time()
        out = fn(*args, **kwargs)
        t2 = time.time()
        print("Elapsed time = ", t2-t1)
        return out

    return inner


@timeit
def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact


res = factorial(30000)
print(res)