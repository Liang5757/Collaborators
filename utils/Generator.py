from utils.Arithmetic import *
import random


class Generator(Arithmetic):

    def __init__(self):
        super(Arithmetic, self).__init__()
        # 操作数个数
        self.operator_num = random.randint(1, 3)