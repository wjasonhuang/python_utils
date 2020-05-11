"""
Continued Fraction
n / d = a0 + 1 / (a1 + 1 / (a2 + ...))
https://en.wikipedia.org/wiki/Continued_fraction

encode(n, d)                n, d => [a0, a1, ...]
decode(a)                   [a0, a1, ...] => n, d
z_func(x, y)                z(x,y) in https://en.wikipedia.org/wiki/Continued_fraction#Best_rational_within_an_interval
between(n1, d1, n2, d2)     returns smallest d such that n1 / d1 < n / d < n2 / d2
"""


def encode(n, d):
    a = []
    while d > 0:
        a.append(n // d)
        r = n % d
        n, d = d, r
    return a


def decode(a):
    n, d = 1, 0
    for ai in reversed(a):
        n, d = ai * n + d, n
    return n, d


def z_func(x, y):
    assert x != y
    lx, ly = len(x), len(y)
    for i in range(max(lx, ly)):
        ax = x[i] if i < lx else y[i] + 1
        ay = y[i] if i < ly else x[i] + 1
        if ax != ay: return x[:i] + [min(ax, ay) + 1]


def between(n1, d1, n2, d2):
    assert n1 * d2 < n2 * d1
    x1, y1 = encode(n1, d1), encode(n2, d2)
    x2, y2 = x1[:-1] + [x1[-1] - 1, 1], y1[:-1] + [y1[-1] - 1, 1]
    ret = []
    for x0 in (x1, x2):
        for y0 in (y1, y2):
            n, d = decode(z_func(x0, y0))
            if n1 * d < n * d1 and n * d2 < n2 * d: ret.append((n, d))
    return sorted(ret, key=lambda x: x[1])[0]
