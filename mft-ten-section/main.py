def decorate(fn):
    def inner(x):
        out = "$"
        out += fn(x)
        out += "$"
        return out

    return inner


@decorate
def say_hello(name):
    return "Hello " + name


res = say_hello("Jack")
print(res)
