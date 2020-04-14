from utils.paser import *
from utils.Generator import *
from views.UserIntrface import *

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
        InitWindows()
    else:
        if (arg.e or arg.a) and (arg.n or arg.r):
            print('Parameter Error')
            exit(0)
        elif arg.a and arg.e:
            inspect(arg.a[0], arg.e[0])
        elif arg.n and arg.r:
            Generator(arg.n[0], arg.r[0]).multi_processor()
        elif arg.n:
            Generator(arg.n[0], 10).multi_processor()
        elif arg.r:
            Generator(10, arg.r[0]).multi_processor()
        else:
            print("HELP INFO: Parameter input ERROR")
