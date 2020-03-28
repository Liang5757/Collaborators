from utils.Arithmetic import *


class Generator(object):

    def __init__(self, num):
        # 表达式个数
        self.expression_num = num
        # 表达式集
        self.expressions = []

    def expression_generator(self):
        while self.expression_num > 1:
            temp = Arithmetic().create_arithmetic()

            if temp:
                self.expressions.append(temp)
                self.expression_num -= 1
            else:
                pass
