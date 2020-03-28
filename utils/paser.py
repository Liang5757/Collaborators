# 指令解析
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-n', '-N', nargs=1, type=int, action='store_true', help='storage number n')

args = parser.parse_args()

print(args)
