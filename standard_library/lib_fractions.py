"""
https://docs.python.org/3/library/fractions.html

fractions.Fraction(numerator=0, denominator=1)
fractions.Fraction(other_fraction)
fractions.Fraction(float)
fractions.Fraction(decimal)
fractions.Fraction(string)

numerator                                       numerator of the Fraction in lowest term
denominator                                     denominator of the Fraction in lowest term
limit_denominator(max_denominator=1000000)      returns the closest Fraction with denominator at most max_denominator

fraction is saved with lowest positive denominator
"""

from fractions import Fraction

a = Fraction(10, -6)
b = Fraction("1.35")
print(a, b, a.numerator, a.denominator)
print(a + b, a * b, a > b, min(a, b), max(a, b))
print(Fraction(3.1415926).limit_denominator(20))
