def gcd(x, y):
    while y != 0:
        t = x % y
        x = y
        y = t
    return x


class Rational:
    def __init__(self, numerator, denominator):
        assert denominator != 0,  'denominator cannot be zero'

        g = gcd(numerator, denominator)
        self.__numerator = numerator // g
        self.__denominator = denominator // g

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def add(self, that):
        return Rational(self.__numerator * that.__denominator + that.__numerator * self.__denominator, self.__denominator * that.__denominator)

    def subtract(self, that):
        return Rational(self.__numerator * that.__denominator - that.__numerator * self.__denominator, self.__denominator * that.__denominator)

    def mul(self, that):
        return Rational(self.__numerator * that.__numerator, self.__denominator * that.__denominator)

    def div(self, that):
        return Rational(self.__numerator * that.__denominator, self.__denominator * that.__numerator)

    def tostring(self):
        return '%d / %d' %(self.__numerator, self.__denominator)


r1 = Rational(1, 2)

r2 = Rational(36, 0)

print(r1.add(r2))
print(r1.subtract(r2))
print(r1.mul(r2))
print(r2.div(r1))
print(r1.tostring())