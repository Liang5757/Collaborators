
# Arithmetic Generator (Python)

[中文](https://github.com/P4XL/Collaborators/blob/master/READMEcn.md)

> **Developer**：[ZeongPaang](https://github.com/P4XL/) / [w1036933220](https://github.com/w1036933220)

----

## 1.  Function realization

- Support parameter [-n] to control the number of generated subjects.
- Support parameter [-r] to control the range* of generated subjects. *(Nature number / improper fraction/ true fraction)*
- The calculation process cannot generate negative numbers in the generated subjects.
- If there is a sub-expression of the form e1 ÷ e2 in the generated subjects, the result should be a true fraction.
- The number of operators appearing in each subject does not exceed 3.
- The subjects generated by the program in one run cannot be repeated.
- While generating the subjects, calculate the answers to all the subjects and store them in the *Answers.txt* file in the current directory of the executing program
- The program should be able to support the generation of 10,000 subjects.
- The program supports the given subjects file and answer file, determine the right and wrong in the answer and count the number
- Graphical user interface

----

##  2.  Packages

> Python version should be python3 and at least it works on Python 3.6 and Python 3.8. Already tested in environments below:
>
> - Windows10 Python 3.6 / 3.7 / 3.8

> Used Packages:
>
> - re / os /  argparse / random

## 3.  Usage

```
$ Python ArithmeticCLMode.py [-args|-args]
```

```
 $ args
    ├─ -h --help    # Output Info
    ├─ -n	    # Specify the number of generated expressions, default 100
    ├─ -r           # Specify the value range of each number in the generated expression, default 100
    ├─ -a           # Need to be used together with the -e parameter for correction and specify the answer file
    ├─ -e           # Need to be used together with the -a parameter for correction and specify the practice file
    └─ g            # GUI mode
```


Example :

> Generate 100 subjects whose domain is in range from 0 to 100
>
> ```python
> python ArithmeticCLMode.py -n 100 -r 100
> ```

> Review files, need Exercise file and Answer file
>
> ```python
> python ArithmeticCLMode.py -e ./docs/Exercise.txt -a ./docs/Answer.txt
> ```

For default config, the file structure should be something like this:

```
Collaborators/
│ .gitingore
│ Arithmetic-CLM.py
│ Arithmetic-GM.py
│ README.md
│ READMEcn.md
├─utils
│  │  Arithmetic.py
│  │  Calculate.py
│  │  constant.py
│  │  Fraction.py
│  │  Generator.py
│  │  Operation.py
│  └─  paser.py
└─views
    └─ UserInterface.py
```

----

## 4.  Bugs

> gui mode must add a nonsense arg : python ./main.py -g xxx
>
> You tell me!

----

## 5.  Cnblog Pages 🚀

- **[Arithmetic Generator (Python)](https://www.cnblogs.com/green--hand/p/12665616.html)**

> [Author :  [ZeongPaang](https://www.cnblogs.com/XL-Lee/) / [w1036933220 ](https://www.cnblogs.com/green--hand/) ]
>
> [Date: Thursday, April 9, 2020]
