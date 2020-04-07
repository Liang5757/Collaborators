# 调用, 生成表达式集
from utils.Calculate import *
from utils.Operation import *
import collections


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
        # 用答案作为索引构建的字典，
        # {
        #     "1'2/2": [
        #         [[压入的数字], [操作数], [运算符]],
        #         [[压入的数字], [操作数], [运算符]]
        #     ]
        # }
        self.no_repeat_dict = {}

    # 根据[压入的数字]判断是否重复
    def judge_repeat(self, answer, test_sign):
        for expression_sign in self.no_repeat_dict[answer]:
            # 记录相同的个数
            same_num = 0

            for i in range(3):
                if collections.Counter(expression_sign[i]) == collections.Counter(test_sign[i]):
                    same_num += 1

            # 如果中间结果、操作数、运算符均相等，则为重复
            if same_num == 3:
                return False

        return True

    # 生成表达式集
    def expression_generator(self):
        while self.expression_num > 0:
            [expression, operand_list, operator_list] = Arithmetic(self.domain).create_arithmetic()
            [answer, stage_results] = Calculate(expression).cal_expression()

            # 如果answer为false，则计算错误
            if answer:
                # 如果该答案不存在字典中，则新建该键值对，否则判断重复，若重复则不添加表达式
                if answer.to_string() in self.no_repeat_dict:
                    if self.judge_repeat(answer.to_string(), [stage_results, operand_list, operator_list]):
                        self.no_repeat_dict[answer.to_string()].append([stage_results, operand_list, operator_list])
                        self.expressions.append(expression)
                        self.answers.append(answer)
                        self.expression_num -= 1
                else:
                    self.no_repeat_dict[answer.to_string()] = [[stage_results, operand_list, operator_list]]
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


Generator(1000).expression_generator()