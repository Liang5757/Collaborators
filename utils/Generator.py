# 调用, 生成表达式集
from utils.Arithmetic import *
from utils.constant import *


class Generator(object):

    def __init__(self, num):
        # 表达式个数
        self.expression_num = num
        # 表达式集
        self.expressions = []
        # 表达式字符串集，用于io写入
        self.expressions_str = []
        # 答案集
        self.answers = []
        # 答案字符串集，用于io写入
        self.answers_str = []

    # 生成表达式集
    def expression_generator(self):
        while self.expression_num > 1:
            temp = Arithmetic().create_arithmetic()

            if temp:
                self.expressions.append(temp)
                self.expression_num -= 1
            else:
                pass

        self.to_string(self.expressions, self.expressions_str)
        print(self.expressions_str)

    # 字符串化
    @staticmethod
    def to_string(material, products):
        for index, element in enumerate(material):
            product = str(index + 1) + ". "

            for item in element:
                if item in operator.values():
                    product += " " + item + " "
                else:
                    product += item

            products.append(product)


Generator(10).expression_generator()
