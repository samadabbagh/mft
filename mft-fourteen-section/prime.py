def is_prime(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True


def prime_generator():
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


gen = prime_generator()

for i, p in enumerate(gen):
    print(i, p)