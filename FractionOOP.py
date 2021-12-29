# -*- coding: utf-8 -*-
# <codecell>Class Definition

class Fraction():
    """A number represented as fraction."""

    def __init__(self, num, denom):
        """Num and denom are integers."""
        assert isinstance(num, int) and isinstance(denom, int)
        self.num = num
        self.denom = denom

    def __str__(self):
        """Return a string representation of self."""
        return '<' + str(self.num) + '/' + str(self.denom) + '>'

    def __add__(self, other):
        """Return a new fraction representing the addition of self and
        other.
        """
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """Return a new fraction representing the subtraction of self and
        other.
        """
        top = self.num * other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __float__(self):
        """Return a float of the fraction."""
        return self.num/self.denom

    def inverse(self):
        """Return new fraction representing the inverse."""
        return Fraction(self.denom, self.num)


# <codecell>Instantiate
a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b

# <codecell>Print
print(c)
print(float(c))
print(float(b.inverse()))

# <codecell>Last

ASDF_1 = 3
ASDF_2 = 2
