def fibo(n):
    if n in (0, 1):
        return n
    return fibo(n - 1) + fibo(n - 2)


def fib_sequence(s):
    for i in range(s):
        print(fibo(i))


s = int(input("enter number"))

if s <= 0:
    print("bozorgtar az 0")
else:
    print("fibonachi:")
    fib_sequence(10)
