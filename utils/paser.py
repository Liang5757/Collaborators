# 指令解析
from argparse import ArgumentParser


def arg_parse():
    parser = ArgumentParser()
    parser.add_argument('-n', nargs=1, type=int, help='the num of generated subject')
    parser.add_argument('-r', nargs=1, type=int, help='the range of generated numbers.')
    parser.add_argument('-e', nargs=1, type=str, help='exercise file')
    parser.add_argument('-a', nargs=1, type=str, help='answer file')
    parser.add_argument('-g', help='GUI mode')
    args = parser.parse_args()
    print(type(args.n[0]))
    return args


if __name__ == '__main__':
    arg_parse()
