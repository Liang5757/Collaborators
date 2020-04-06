from utils.paser import *
# from utils.Arithmetic import *
from utils.Calculate import *
from utils.Operation import *
from utils.Generator import *

"""
::param '-n': type=int, help=' the num of generated subject'
::param '-r': type=int, help=' the range of generated numbers.'
::param '-e': type=str, help=' exercise file'
::param '-a': type=str, help=' answer file'
::param '-g':           help=' GUI mode'
"""

if __name__ == '__main__':

    arg = arg_parse()

    # 是否开启GUI
    if arg.g:
        print('GUI mode not finished')
    else:
        if (arg.e or arg.a) and (arg.n or arg.r):
            print('Parameter Error')
            exit(0)
        elif arg.a and arg.e:
            pass
        elif arg.n and arg.r:
            Generator(arg.n[0], arg.r[0]).expression_generator()
        elif arg.n:
            Generator(arg.n[0], 10).expression_generator()
        elif arg.r:
            Generator(10, arg.r[0]).expression_generator()
        else:
            print("HELP INFO: Parameter input ERROR")
