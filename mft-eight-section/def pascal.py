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
def pascal_row(n):
    res = []
    for i in range(n+1):
        tmp = combination(n, i)
        res.append(tmp)
    return res


def pascal(n):
    res = []
    for i in range(n):
        res.append(pascal_row(i))
    return res

if __name__ == '__main__':
    for i in range(10):
        print(pascal_row(i))
    print(pascal(10))