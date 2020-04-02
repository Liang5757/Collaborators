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

    # 生成表达式集
    def expression_generator(self):
        while self.expression_num > 1:
            temp = Arithmetic().create_arithmetic()

            if temp:
                self.expressions.append(temp)
                self.expression_num -= 1
            else:
                pass

        self.to_string()
        print(self.expressions_str)

    # 表达式字符串化
    def to_string(self):
        for index, expression in enumerate(self.expressions):
            str_ex = str(index + 1) + ". "

            for item in expression:
                if item in operator.values():
                    str_ex += " " + item + " "
                else:
                    str_ex += item

            self.expressions_str.append(str_ex)


Generator(10).expression_generator()
