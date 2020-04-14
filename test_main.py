from utils.paser import *
from utils.Generator import *
from views.UserIntrface import *
from views.UserIntrface import *

"""
::param '-n': type=int, help=' the num of generated subject'
::param '-r': type=int, help=' the range of generated numbers.'
::param '-e': type=str, help=' exercise file'
::param '-a': type=str, help=' answer file'
::param '-g':           help=' GUI mode'
"""

if __name__ == '__main__':

    Generator(100, 100).multi_processor()
    # print(InitWindows)
