from time import ctime


def log(fn):
    def inner(*args, **kwargs):
        res = fn(*args, **kwargs)
        f = open('output.log', mode='a')
        f.write(ctime() + " | " + fn.__name__ + " | " + str(args) + str(kwargs) + " | " + str(res) + "\n")
        f.close()
        return res

    return inner


@log('output1.log')
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact


@log('out2.log')
def mysum(a, b):
    out = a + b
    return out


factorial(10)
mysum(10, 20)
factorial(2)
factorial(5)