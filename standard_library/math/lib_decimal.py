"""
https://docs.python.org/3/library/decimal.html

decimal.Decimal(value="0", context=None)
    value can be an integer, string, tuple, float, or another Decimal object

adjusted()                      return the adjusted exponent
as_integer_ratio()              return a pair (n, d) of integers that represent the given Decimal instance as a fraction
as_tuple()                      return a named tuple DecimalTuple(sign, digits, exponent)
copy_abs()                      return the absolute value of the argument
copy_sign(other)                return a copy of the first operand with the sign set to be the same as other
exp()                           return the value of the (natural) exponential function e**x at the given number
quantize(exp, rounding=None)    round a number to a fixed exponent

Rounding modes
decimal.ROUND_CEILING           round towards Infinity
decimal.ROUND_FLOOR             round towards -Infinity
decimal.ROUND_UP                round away from zero
decimal.ROUND_DOWN              round towards zero
decimal.ROUND_HALF_UP           round to nearest with ties going away from zero.
decimal.ROUND_HALF_DOWN         round to nearest with ties going towards zero
decimal.ROUND_HALF_EVEN         round to nearest with ties going to nearest even integer
"""

import decimal
from decimal import Decimal

a = Decimal(-139) + Decimal('-2e-5') + Decimal('1.53')
print(a)
print(a.adjusted())  # the position of the most significant digit with respect to the decimal point
print(a.as_integer_ratio())
print(a.as_tuple())  # sign 0 for positive or 1 for negative
print(a.copy_abs(), a.quantize(Decimal('1.000'), rounding=decimal.ROUND_UP))
b = Decimal(15)
print(a, b, a + b, a - b, a * b, a / b)
