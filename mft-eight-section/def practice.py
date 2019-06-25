def factorial(t):
    """
        computes factorial  .blaah blaah
        :param t: an integer number
        :return: factorial
        """
    res = 1
    while t:
        res = res * t
        t -= 1

    return res


def combination(m, n):
    val_1 = factorial(m)
    val_2 = factorial(n)
    val_3 = factorial(m - n)

    c = val_1 / (val_2 * val_3)
    return int(c)


for i in range(10):
    print(combination(9, i))