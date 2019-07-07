def red(fn):
    def inner(x):
        out = "\033[31" + "m"
        out += fn(x)
        out += "\033[0m"
        return out

    return inner


def green(f):
    def inner_1(y):
        out = "\033[32" + "m"
        out += f(y)
        out += "\033[0m"
        return out

    return inner_1


def blue(fn):
    def inner_3(p):
        out = "\033[34" + "m"
        out += fn(p)
        out += "\033[0m"
        return out

    return inner_3


def bold(l):
    def bold_inner(w):
        out = "\033[3;1m"
        out += l(w)
        out += "\033[1m"
        return out

    return bold_inner


def underline(d):
    def underline_inner(w):
        out = "\033[3;4m"
        out += d(w)
        out += "\033[4m"
        return out

    return underline_inner


def revert(n):
    def revert_inner(w):
        out = "\033[3;7m"
        out += n(w)
        out += "\033[7m"
        return out

    return revert_inner


def highlight(k):
    def highlight_inner(i):
        out = "\033[40;m"
        out += k(i)
        out += "\033[m"
        return out

    return highlight_inner


def exaggerate(j):
    def exaggerate_inner(g):
        out = "\033[9;m"
        out += j(g)
        out += "\033[m"
        return out

    return exaggerate_inner

@red
@bold
def echo(s):
    return "hello " + s


print(echo("nazanin"))


@highlight
@underline
@green
@revert
def echo_2(e):
    return "hello " + e


print(echo_2("samaneh"))


@blue
@exaggerate
@bold
def echo_3(d):
    return "hello" + d


print(echo_3(" sama"))
