# 调用, 生成表达式集
from utils.Calculate import *
from utils.Operation import *


class Generator(object):

    def __init__(self, num=10, domain=10):
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
        self.domain = domain

    # 生成表达式集
    def expression_generator(self):
        while self.expression_num > 0:
            expression = Arithmetic(self.domain).create_arithmetic()
            # print(expression)

            # 生成阶段去重
            if expression not in self.expressions:
                answer = Calculate(expression).cal_expression()

                if answer:
                    self.expressions.append(expression)
                    self.answers.append(answer)
                    self.expression_num -= 1

        # 表达式和答案字符串化成io所需格式
        self.expression_stringify()
        self.answer_stringify()

        # 保存
        save_exercise(self.expressions_str)
        save_answer(self.answers_str)


    # 表达式集字符串化
    def expression_stringify(self):
        for index, expression in enumerate(self.expressions):
            expression_str = str(index + 1) + ". "

            for item in expression:
                if item in operator.values():
                    expression_str += " " + item + " "
                else:
                    expression_str += item

            self.expressions_str.append(expression_str)

    # 答案集字符串化
    def answer_stringify(self):
        for index, answer in enumerate(self.answers):
            answer_str = str(index + 1) + ". "
            answer_str += answer.to_string()

            self.answers_str.append(answer_str)