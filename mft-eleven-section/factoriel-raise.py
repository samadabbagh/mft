def fac(m):
    if not type(m) == int:
        raise SyntaxWarning("enter int number ")

    if m < 0:
        raise SyntaxWarning("enter positive number")

    out = 1
    while m > 0:
        out *= m
        m -= 1
    return out


print(fac(8.5))
