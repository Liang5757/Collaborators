# 表达式的类, 放回表达式
import random
from utils.constant import *
from utils.paser import arg_parse


class Arithmetic(object):

    def __init__(self, domain=arg_parse().r[0]):
        # 运算符个数
        self.operator_num = random.randint(1, 3)
        # 操作数个数
        self.operand_num = self.operator_num + 1
        # 取值范围
        self.domain = domain
        # 是否有括号
        self.has_bracket = random.randint(0, 1)
        # 运算符集
        self.operator_list = []
        # 操作数集
        self.operand_list = []
        # 表达式
        self.expression = ""
        # 储存题目
        self.exercise = []
        # 储存答案
        self.answer = []

    # 生成随机操作数(自然数0、真分数1)
    def random_number(self):
        num_type = random.randint(0, 1)
        number = ""

        if num_type == 0:
            # 不包括self.domain
            number = str(random.randint(0, self.domain - 1))
        elif num_type == 1:
            # 整数部分
            z = random.randint(0, self.domain - 1)
            # 分母
            denominator = random.randint(2, self.domain - 1)
            # 分子
            molecular = random.randint(1, denominator - 1)

            if z != 0:
                number = str(z) + '\'' + str(molecular) + "/" + str(denominator)
            else:
                number = str(molecular) + "/" + str(denominator)

        return number

    # 生成随机操作数集
    def create_operand_list(self):
        num = self.operand_num

        while num:
            self.operand_list.append(self.random_number())
            num -= 1

    # 生成随机运算符集
    def create_operator_list(self):
        num = self.operator_num

        while num:
            self.operator_list.append(operator[random.randint(0, 3)])
            num -= 1

    # 随机产生括号的位置
    def random_bracket_place(self):
        while 1:
            left_bracket = random.randint(1, self.operand_num - 1)
            right_bracket = random.randint(left_bracket + 1, self.operand_num)

            # 类似(1 + 2 + 3)的位置则重新随机
            if left_bracket == 1 and right_bracket == self.operand_num:
                continue
            else:
                return [left_bracket, right_bracket]

    # 处理括号
    def insert_space(self, bracket_num):
        # 存放分离化的表达式
        expression_split = []

        expression_split.append(self.operand_list.pop()).append(" ").append(self.operator_list.pop())
        while self.operator_list:
            expression_split.append(" ").append(self.operand_list.pop()).append(" ").append(self.operator_list.pop())
        expression_split.append(" ").append(self.operand_list.pop())

        while bracket_num:
            # 随机括号位置，相对于数字的位置
            bracket_place = self.random_bracket_place()

    def create_arithmetic(self):
        self.create_operand_list()
        self.create_operator_list()

        if self.operator_num == 1 or self.has_bracket == 0:
            self.expression += (self.operand_list.pop() + " " + self.operator_list.pop())
            while self.operator_list:
                self.expression += (" " + self.operand_list.pop() + " " + self.operator_list.pop())
            self.expression += " " + self.operand_list.pop()
        else:
            bracket_num = random.randint(1, self.operator_num - 1)


Arithmetic().create_arithmetic()
