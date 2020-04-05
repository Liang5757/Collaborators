from utils.paser import arg_parse
from utils.Arithmetic import *
from utils.Generator import *


if __name__ == '__main__':
    # return args from command line
    agr = arg_parse()
    if agr.g:
        # GUI on
        pass
    else:
        # GUI off
        pass

Generator(num=10, domain=10).expression_generator()