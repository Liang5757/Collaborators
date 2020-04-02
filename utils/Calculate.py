from utils.Fraction import *


class Calculate(object):

    def __init__(self, expression):
        self.expression = expression

    def test(self):
        fra1 = Fraction("6'4/6")
        fra2 = Fraction("0")
        print(self.fraction_divide(fra1, fra2).to_string())

    # 分数加法 a1/b1 + a2/b2 = (a1b2 + a2b1)/b1b2
    @staticmethod
    def fraction_add(fra1, fra2):
        molecular = fra1.molecular * fra2.denominator + fra2.molecular * fra1.denominator
        denominator = fra1.denominator * fra2.denominator

        return Fraction(molecular, denominator)

    # 分数减法 a1/b1 - a2/b2 = (a1b2 - a2b1)/b1b2
    @staticmethod
    def fraction_minus(fra1, fra2):
        molecular = fra1.molecular * fra2.denominator - fra2.molecular * fra1.denominator
        denominator = fra1.denominator * fra2.denominator

        return Fraction(molecular, denominator)

    # 分数乘法 a1/b1 * a2/b2 = a1a2/b1b2
    @staticmethod
    def fraction_multiply(fra1, fra2):
        molecular = fra1.molecular * fra2.molecular
        denominator = fra1.denominator * fra2.denominator

        return Fraction(molecular, denominator)

    # 分数除法 a1/b1 ÷ a2/b2 = a1b2/a2b1
    @staticmethod
    def fraction_divide(fra1, fra2):
        molecular = fra1.molecular * fra2.denominator
        denominator = fra1.denominator * fra2.molecular

        return Fraction(molecular, denominator)


Calculate("").test()
