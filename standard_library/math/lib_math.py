"""
https://docs.python.org/3/library/math.html

math.ceil(x)                the smallest integer greater than or equal to x
math.copysign(x, y)         a float with absolute value of x but the sign of y
math.fabs(x)                a float with absolute value of x
math.factorial(x)
math.floor(x)               the largest integer less than or equal to x
math.fmod(x, y)             x - n * y, n integer, same sign as x, magnitude < abs(y)
math.fsum(iterable)         return an accurate floating point sum of values in the iterable
math.gcd(a, b)

math.inf                    float('inf')
math.nan                    float('nan')
math.isinf(x)               True if x is a positive or negative infinity, and False otherwise 
math.isnan(x)               True if x is a NaN (not a number), and False otherwise

math.e                      2.718281828459045
math.exp(x)                 usually more accurate than math.e ** x
math.expm1(x)               exp(x) - 1 compute to full precision
math.log(x[, base=e])
math.log1p(x)               ln(1 + x) more accurate for x near zero
math.log2(x)
math.log10(x)
math.pow(x, y)              a float = x ** y
math.sqrt(x)

math.pi                     3.141592653589793
math.sin(x)                 sine of x radians
math.cos(x)                 cosine of x radians
math.tan(x)                 tangent of x radians
math.asin(x)                inverse sine
math.acos(x)                inverse cosine
math.atan(x)                inverse tangent
math.atan2(y, x)            return atan(y / x) in radians, between -pi and pi
"""

import math


def lcm(a, b): return a * b // math.gcd(a, b)


print(math.copysign(1, -1))
print(math.fmod(-5, 1.1))
print(lcm(6, 4))
print(math.isinf(math.inf), math.isinf(-2 * math.inf + 1))
print(math.isnan(float('nan')), math.isnan(-2 * math.nan + 1))
print(math.sqrt(2), math.sqrt(3), math.sqrt(5))
print(math.sin(math.pi / 3), math.cos(math.pi / 3), math.tan(math.pi / 3))
print(math.asin(0.5), math.acos(0.5))
