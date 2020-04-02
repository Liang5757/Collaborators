# 计算类
from utils.Fraction import *
from utils.Arithmetic import *
from utils.constant import *


class Calculate(object):

    def __init__(self, expression):
        self.expression = expression

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

    # 逆波兰
    def generate_postfix_expression(self):
        # 操作符栈
        operator_stack = []
        # 表达式队列
        expression_stack = []

        for element in self.expression:
            # 如果数字进入表达式栈
            if element in operators:
                # 左括号进栈, 如果栈空, 操作符直接进操作符栈
                if not operator_stack:
                    operator_stack.append(element)
                else:
                    # 若操作符是右括号, 操作符栈出栈直至遇到左括号
                    # 操作符中除了括号全都进表达式队列
                    if element == ")":
                        for top in operator_stack[::-1]:
                            if top != "(":
                                expression_stack.append(top)
                                operator_stack.pop()
                            else:
                                operator_stack.pop()
                                break
                    else:
                        for top in operator_stack[::-1]:
                            # 目标元素大于栈顶元素则入栈 否则出栈并入栈到队列中
                            if priority[top] >= priority[element] and top != "(":
                                expression_stack.append(top)
                                operator_stack.pop()
                            else:
                                operator_stack.pop()
                                break
                        # 如果操作符栈所有元素优先级都大于目标操作符优先级 操作符则全部出栈
                        if not operator_stack:
                            operator_stack.append(element)
            else:
                expression_stack.append(element)
        # 中序遍历完毕 若仍有操作符 操作栈的操作符入表达式栈中
        for index in range(len(operator_stack)):
            expression_stack.append(operator_stack.pop())

        return expression_stack

    def calcaulate(self):
        # 生成后缀表达式
        expressions_result = self.generate_postfix_expression()
        print(expressions_result)
        # 使用list作为栈来计算
        calcalate_stack = []

        # 后缀遍历
        for element in expressions_result:
            # 若是数字则入栈, 操作符则将栈顶两个元素出栈
            if element not in operators:
                calcalate_stack.append(element)
            else:
                # 操作数
                num1 = calcalate_stack.pop()
                # 操作数
                num2 = calcalate_stack.pop()
                # 结果
                result = self.operate(num2, num1, element)
                # 结果入栈
                calcalate_stack.append(result)
                print(calcalate_stack)
        # 返回结果
        return calcalate_stack[0]

    def operate(self, num1, num2, operater):
        if not isinstance(num1, Fraction):
            num1 = Fraction(num1)
        if not isinstance(num2, Fraction):
            num2 = Fraction(num2)

        # 计算结果
        if operater == '+':
            return self.fraction_add(num1, num2)
        if operater == '-':
            return self.fraction_minus(num1, num2)
        if operater == '×':
            return self.fraction_multiply(num1, num2)
        if operater == '÷':
            return self.fraction_divide(num1, num2)


if __name__ == '__main__':

    expressions = ['7', '×', '(', '2', '-', '0', ')']
    c = Calculate(expressions)
    expression_result = c.calcaulate()
    print(expression_result)
    # 返回结果
