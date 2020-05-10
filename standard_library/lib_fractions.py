"""
https://docs.python.org/3/library/fractions.html

fractions.Fraction(numerator=0, denominator=1)
fractions.Fraction(other_fraction)
fractions.Fraction(float)
fractions.Fraction(decimal)
fractions.Fraction(string)

numerator                                       numerator of the Fraction in lowest term
denominator                                     denominator of the Fraction in lowest term
as_integer_ratio()                              return a tuple of two integers with a positive denominator
from_float(flt)
from_decimal(dec)
limit_denominator(max_denominator=1000000)      returns the closest Fraction with denominator at most max_denominator
"""

import fractions
